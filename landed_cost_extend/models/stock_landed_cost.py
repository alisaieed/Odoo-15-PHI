# -*- coding: utf-8 -*-

from odoo import models, api, _, fields
from odoo.exceptions import UserError, ValidationError


class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    credit_account_id = fields.Many2one('account.account', 'Credit Account', states={'done': [('readonly', True)]})

    def button_validate(self):
        res = super(StockLandedCost, self).button_validate()
        self.account_move_id.button_draft()
        for l in self.account_move_id.line_ids:
            l.sudo().with_context(check_move_validity=False, force_delete=True).unlink()

        total_cost = 0.0
        AccountMoveLine = []
        for sl in self.cost_lines:
            lines = {
                'name': sl.name,
                'product_id': sl.product_id.id,
                'quantity': 1,
                'account_id': sl.account_id.id,
                'debit': sl.price_unit,
                'credit': 0,
            }
            AccountMoveLine.append([0, 0, lines])
            total_cost += sl.price_unit

        if AccountMoveLine:
            credit_lines = {
                'name': 'credit value',
                'product_id': 0,
                'quantity': 1,
                'account_id': self.credit_account_id.id,
                'debit': 0,
                'credit': total_cost,
            }
            AccountMoveLine.append([0, 0, credit_lines])

        self.account_move_id.line_ids = AccountMoveLine
