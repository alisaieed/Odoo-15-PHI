# -*- coding: utf-8 -*-
# Part of Axistechnolabs Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api, _
import datetime
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    number = fields.Char('Ticket Id', readonly=True)
    timesheet_ids = fields.One2many('account.analytic.line','ticket_id','Timesheet')
    move_line_ids = fields.One2many('account.move.line', 'ticket_id', 'Account')
    project_project_id= fields.Many2one('project.project',string="Project")
    is_task = fields.Boolean()
    is_invoice = fields.Boolean()
    is_task_button =fields.Boolean()
    is_invoice_button =fields.Boolean()
    invoice_payment_term_id = fields.Many2one('account.payment.term',string='Payment Terms')
    journal_id = fields.Many2one('account.journal',string='Journal')   
    close_ticket = fields.Boolean()
    ticket_invoice_ids = fields.One2many('helpdesk.ticket.invoice', 'ticket_id', 'Ticket Invoice')
    partner_id = fields.Many2one('res.partner')
    is_invoice = fields.Boolean('Is Invoice', readonly=True)
    invoice_number= fields.Char(string="Invoice Number")
    product = fields.Many2one('product.product',string='Product')
    serial_number= fields.Many2one('stock.production.lot',string='Serial Number')
    stock_location= fields.Many2one('stock.location',string='Stock Location')

    warranty_year = fields.Char(string='Warranty Period')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    partner_phone = fields.Char(string='Customer Phone')
    partner_address = fields.Char(string='Customer Address')
    is_repair_button = fields.Boolean()
    repair = fields.Many2one('repair.order',string='Repair',  tracking=True)
    account_detail = fields.Many2one('account.move',string='Account', tracking=True)
    partner_street2 = fields.Char()
    partner_city = fields.Char()
    partner_state = fields.Char()
    partner_zip= fields.Char()
    partner_country = fields.Char()



    @api.onchange('start_date')
    def _onchange_warranty_dates(self):
        search = self.env['stock.production.lot'].search([('name','=',self.serial_number.name)])
        search.start_date = self.start_date
        search.end_date = self.start_date
        format_str = '%Y%m%d'
        if self.start_date:
            warranty_year = int(self.warranty_year) * 365
            a = self.start_date
            abcd = str(a).replace('-', '')
            start_date_info = datetime.datetime.strptime(abcd,format_str)
            self.end_date = start_date_info + datetime.timedelta(days=warranty_year)



    @api.onchange('end_date')
    def _onchange_operation_type(self):
        search = self.env['stock.production.lot'].search([('name','=',self.serial_number.name)])
        search.end_date = self.end_date

    @api.onchange('warranty_year')
    def _onchange_ope(self):
        search = self.env['stock.production.lot'].search([('name','=',self.serial_number.name)])
        search.warranty_year = self.warranty_year



    @api.onchange('serial_number')
    def _onchange_s1erial(self):
        search = self.env['stock.production.lot'].search([('name','=',self.serial_number.name)])
        self.warranty_year  = search.warranty_year   
        self.end_date  = search.end_date   
        self.start_date  = search.start_date



    @api.onchange('product')
    def _onchange_product(self):
        self.serial_number = ''


    def repair_button(self):
        self.is_repair_button = True
        repair_id = self.env['repair.order'].create({
                'partner_id': self.partner_id.id,
                'product_id': self.product.id,
                'product_uom': self.product.uom_id.id,
                'guarantee_limit' :self.end_date,
                'lot_id':self.serial_number.id,
                'location_id': self.stock_location.id,
                })

        search_record = self.env['repair.order'].search([('partner_id','=',self.partner_id.id),
            ('product_id','=',self.product.id), ('lot_id','=',self.serial_number.id)])[0]
        self.repair = search_record.id


        return {
                'name': _('Create Repair'),
                'view_mode': 'form,list',
                'res_model': 'repair.order',
                'res_id': search_record.id,
                'type': 'ir.actions.act_window',
                }

    def create_task(self):
        self.is_task= True
        task_id = self.env['project.task'].create({
                'name': self.name,
                'project_id': self.project_project_id.id,
                'user_ids' : self.user_id.ids,
                'description': self.description,
                })

    def task_action(self):
        self.is_task_button = True
        search_record = self.env['project.task'].search([('name','=',self.name),('user_ids','in',self.user_id.ids),('description','=',self.description),('project_id','=',self.project_project_id.id)])
        if search_record:
            return {
                'name': _('Create Task'),
                'view_mode': 'form',
                'res_model': 'project.task',
                'res_id': search_record.id,
                'type': 'ir.actions.act_window',
                }


    def create_invoice(self):
        self.is_invoice = True
        if self.ticket_invoice_ids:
            move = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': self.partner_id.id,
                'date': datetime.datetime.now(),
            })
            for product in self.ticket_invoice_ids:
                move.write({

                    'invoice_line_ids': [
                        (0, 0, {
                            'product_id': product.product_id,
                            'product_uom_id': False,
                            'quantity':  product.quantity,
                            'price_unit': product.price_unit,
                            'tax_ids': product.product_id.taxes_id,
                        }),
                    ]
                })

            move.action_post()

            self.write({
                'is_invoice': True,
                'invoice_number': move.id,

            })

    def invoice_action(self):
        self.is_invoice_button = True
        search_invoice = self.env['account.move'].search([('partner_id','=',self.partner_id.id),
            ('id','=',self.invoice_number)])
        self.account_detail = search_invoice.id
        return {
                'name': _('Create Invoice'),
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': search_invoice.id,
                'type': 'ir.actions.act_window',
                }


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    ticket_id = fields.Many2one('helpdesk.ticket','Ticket')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    ticket_id = fields.Many2one('helpdesk.ticket', 'Ticket')
    product_id_new = fields.Many2one('product.product',string="Product")


class HelpdeskTicketInvoice(models.Model):
    _name = 'helpdesk.ticket.invoice'
    _description = "Helpdesk Ticket Invoice"

    product_id = fields.Many2one('product.product', 'Product',required=True)
    name = fields.Char(related='product_id.name',string='Lable',required=True)
    tax = fields.Char(string='Tax')
    quantity = fields.Float('Quantity',default=1)
    price_unit = fields.Float(related='product_id.list_price', string='Price')
    ticket_id = fields.Many2one('helpdesk.ticket', 'First')


    @api.onchange('quantity')
    def _onchange_quantity(self):
        for record in self:
            search = record.env['product.product'].sudo().search([('name','=',record.product_id.name)])
            for rec in search:
                record.price_unit = record.quantity * rec.list_price


    @api.onchange('product_id')
    def _onchange_tax(self):
        for record in self:
            search = record.env['product.product'].sudo().search([('name','=',record.product_id.name)])
            for rec in search:
                record.tax = search.taxes_id.name


