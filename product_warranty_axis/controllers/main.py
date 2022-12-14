# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import odoo



class WebsiteManageHelpdesk(http.Controller):

    @http.route('/search_helpdesk_tickets', type='http', auth='user', website=True)
    def search_create_helpdesk_tickets_details(self , **kwargs):
        helpdesk_tickets = request.env['helpdesk.ticket'].sudo().search([])
        return  request.render('product_warranty_axis.search_helpdesk_ticket_page', {'ticket': helpdesk_tickets})

    @http.route(['/helpdesk/search/ticket'], type='http', methods=['POST'],auth='user', website=True, csrf=False)
    def helpdesk_search_ticket(self , **kwargs):
        ticket_id = request.env['helpdesk.ticket'].search([('number','=', kwargs.get('search'))])
        if ticket_id:
            return request.redirect('/helpdesk/ticket/%s' % (ticket_id.id))
        else:
            return request.render('product_warranty_axis.helpdesk_error_message', {'error_message': ticket_id})



    @http.route(['/helpdesk/form'], type='http', auth="public", website=True)
    def helpdesk_form(self, **post):
        helpdesk_tickets = request.env['helpdesk.ticket'].sudo().search([])
        helpdesk_tickets_type = request.env['helpdesk.ticket.type'].sudo().search([])
        product_lot_id = request.env['product.product'].sudo().search([['is_warranty', '=', True]])
       
        return request.render("product_warranty_axis.tmp_helpdesk_ticket_form", 
            {'my_tickets': helpdesk_tickets,'ticket_types': helpdesk_tickets_type,
            'product_w':product_lot_id})
        

    @http.route(['/helpdesk/form/submit'], type='http', auth="public", website=True)
    def helpdesk_form_submit(self, **post):    
        if not post:
            return request.redirect("/helpdesk/form")

        lot_id = request.env['stock.production.lot'].sudo().search([('product_id.id','=', post.get('product')),('name','=', post.get('serial_number'))])
        if lot_id :
            userid = request.env['res.partner'].sudo().search([('email','=', post.get('partner_email'))])
            if not userid:
                userid.create({
                    'name': post.get('partner_name'),
                    'email': post.get('partner_email'),
                    'phone': post.get('partner_phone'),
                    })
            if lot_id.partner_email:
                if lot_id.partner_email == userid.email:
                    ticket = request.env['helpdesk.ticket'].sudo().create({
                        'ticket_type_id': post.get('ticket_type_id'),
                        'name': post.get('name'),
                        'partner_name': post.get('partner_name'),
                        'partner_email': post.get('partner_email'),
                        'priority': post.get('priority'),
                        'description': post.get('description'),
                        'partner_phone': post.get('partner_phone'),
                        'product': post.get('product'),
                        'serial_number':lot_id.id,
                        'warranty_year':lot_id.warranty_year,
                        'start_date':lot_id.start_date,
                        'end_date':lot_id.end_date
                    })   
                    vals = {
                        'ticket': ticket,
                    }
                    return request.render("product_warranty_axis.tmp_helpdesk_ticket_form_success", vals)
                else:
                    return request.render("product_warranty_axis.error_message")
                    
            else:
                userid = request.env['res.partner'].sudo().search([('email','=', post.get('partner_email'))])
                lot_id.write({
                    'partner_id': userid,
                    'partner_email': post.get('partner_email'),
                    'partner_phone': post.get('partner_phone'),
                    })
                ticket = request.env['helpdesk.ticket'].sudo().create({
                    'ticket_type_id': post.get('ticket_type_id'),
                    'name': post.get('name'),
                    'partner_name': post.get('partner_name'),
                    'partner_email': post.get('partner_email'),
                    'priority': post.get('priority'),
                    'description': post.get('description'),
                    'partner_phone': post.get('partner_phone'),
                    'product': post.get('product'),
                    'serial_number':lot_id.id,
                    'warranty_year':lot_id.warranty_year,
                    'start_date':lot_id.start_date,
                    'end_date':lot_id.end_date
                })   
                vals = {
                    'ticket': ticket,
                }
                return request.render("product_warranty_axis.tmp_helpdesk_ticket_form_success", vals)

        else:
            if not post.get('serial_number'): 
                ticket = request.env['helpdesk.ticket'].sudo().create({
                        'ticket_type_id': post.get('ticket_type_id'),
                        'name': post.get('name'),
                        'partner_name': post.get('partner_name'),
                        'partner_email': post.get('partner_email'),
                        'priority': post.get('priority'),
                        'description': post.get('description'),
                        'partner_phone': post.get('partner_phone'),
                        'product': post.get('product'),
                        })
                vals = {
                    'ticket': ticket,
                }

                return request.render("product_warranty_axis.tmp_helpdesk_ticket_form_success", vals)
            else:
                return request.render("product_warranty_axis.error_message_serial")
    