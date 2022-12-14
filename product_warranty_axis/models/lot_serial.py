# -*- coding: utf-8 -*-
# Part of Axistechnolabs Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
import datetime
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta



class Lots(models.Model):
    _inherit = 'stock.production.lot'

    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    warranty_year = fields.Char(string='Warranty Period', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    partner_email = fields.Char(string='Customer Email', tracking=True)
    partner_phone = fields.Char(string='Customer Phone', tracking=True)
    partner_name = fields.Char(string='Customer Name')
    po_id = fields.Many2one('purchase.order', 'Purchase Order')
    so_id = fields.Many2one('sale.order', 'Sale Order')
    installation_date = fields.Date('Installation date')
    end_user_id = fields.Many2one('res.users', 'User')
    end_partner_id = fields.Many2one('res.partner', string='End Customer', tracking=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_name = self.partner_id.name
            self.partner_email = self.partner_id.email
            self.partner_phone = self.partner_id.mobile

    @api.onchange('warranty_year')
    def _onchange_w(self):
        search = self.env['helpdesk.ticket'].search([('serial_number','=',self.name),('partner_id','=',self.partner_id.id)])
        search.warranty_year = self.warranty_year

    @api.onchange('start_date')
    def _onchange_start_date(self):
        search = self.env['helpdesk.ticket'].search([('serial_number','=',self.name),('partner_id','=',self.partner_id.id)])
        search.start_date = self.start_date

    @api.onchange('start_date')
    def _onchange(self):
        search = self.env['helpdesk.ticket'].search([('serial_number','=',self.name)])
        search.start_date = self.start_date
        search.end_date = self.start_date
        format_str = '%Y%m%d'
        if self.start_date:
            warranty_year = int(self.warranty_year) * 365
            a = self.start_date
            abcd = str(a).replace('-', '')
            date_str = '29122017'
            start_date_info =   datetime.datetime.strptime(abcd,format_str)
            self.end_date = start_date_info + datetime.timedelta(days=warranty_year)

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.start_date and self.end_date:
            diff = (self.end_date-self.start_date).days
            self.warranty_year = str(diff) + ' Days'


class ProductTemplateInherit(models.Model):
    _inherit = ['product.template']

    is_warranty = fields.Boolean(string="Can be warranty")

