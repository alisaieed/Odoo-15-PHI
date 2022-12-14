# -*- coding: utf-8 -*-

from odoo import models, api, _, fields
from odoo.exceptions import UserError, ValidationError


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    def action_sheet_move_create(self):
        res = super(HrExpenseSheet, self).action_sheet_move_create()
        for expense in res:
            for move in res[expense]:
                if len(move.line_ids) > 2:
                    move.button_draft()
                    total_credit = sum(move.line_ids.mapped('credit'))
                    credit_line_ids = move.line_ids.filtered(lambda m: m.credit > 0.0)
                    count = 0
                    len_lines = len(credit_line_ids)
                    for line in credit_line_ids:
                        if count != len_lines - 1:
                            line.sudo().with_context(check_move_validity=False, force_delete=True).unlink()
                        else:
                            final_line = line
                        count += 1

                    if final_line:
                        final_line.with_context(check_move_validity=False).credit = total_credit
                        final_line.name = self.name
        return res


class HrExpense(models.Model):
    _inherit = "hr.expense"

    payment_mode = fields.Selection([
        ("own_account", "Employee (to reimburse)"),
        ("company_account", "Company")
    ], default='company_account', states={'done': [('readonly', True)], 'approved': [('readonly', True)], 'reported': [('readonly', True)]}, string="Paid By")
