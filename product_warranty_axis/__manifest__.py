# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Warranty Management in odoo, Product warranty registration, Product Warranty Claim, Verify and set warranty period days, months, years, Helpdesk for customer ticket support',
    'version': '15.0.1',
    'category': 'Operations/Helpdesk',
    'sequence': 57,
    'summary': 'Create, manage products warranty and claims product warranty in odoo, product warranty registration Helpdesk for customer ticket support Product Warranty Management Product Warranty Claim warranty module claim Warranty Maintenance Customer Service Management manage warranty app website product Warranty product Maintenance product service warranty serial number claim Warranty renewal Warranty product Warranty register product Warranty product warranty serial number Registration',
    'depends': [
        'base_setup',
        'mail',
        'utm',
        'rating',
        'web_tour',
        'resource',
        'portal',
        'digest',
        'sale_management',
        'hr',
        'sale_timesheet',
        'project',
        'account',
        'website',
        'hr_timesheet',
        'web',
        'board',
        'contacts',
        'stock',
        'repair',
        
    ],
    'description': """
Product Warranty Management in odoo, Product Warranty Claim, Verify and set warranty period days, months, years, elpdesk - Ticket Support App

Features:

    - Process of customer tickets through different stages to solve them.
    - Add priorities, types, descriptions and tags to define your tickets.
    - Use the chatter to communicate additional information and ping co-workers on helpdesk tickets.
    - Enjoy the use of an adapted dashboard, and an easy-to-use kanban view to handle your ticket portal.
    - Make an in-depth analysis of your tickets through the pivot view in the reports menu.
    - Create a team and define its members, use an automatic assignment method if you wish.
    - Use a mail alias to automatically create tickets and communicate with your customers.
    - Add Service Level Agreement deadlines automatically to your Odoo website helpdesk Tickets.
    - Get customer feedback by using ratings.
    - Install additional features easily using your team form view.

    """,
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/digest_data.xml',
        'data/mail_data.xml',
        'data/helpdesk_sequence_number.xml',
        'data/helpdesk_data.xml',
        'data/web_menu.xml',
        'views/helpdesk_views.xml',
        'views/helpdesk_team_views.xml',
        # 'views/assets.xml',
        'views/digest_views.xml',
        'views/helpdesk_portal_templates.xml',
        'views/res_partner_views.xml',
        'views/mail_activity_views.xml',
        'views/create_helpdesk_ticket.xml',
        'views/search_ticket_view.xml',
        'views/summary_view.xml',
        'views/product_template_inherit.xml',
        'views/lot_serial_view.xml',
        'views/product_warranty.xml',
        'views/regsitration_error.xml', 
        'report/helpdesk_sla_report_analysis_views.xml',
    ],
    # 'qweb': [
    #     "static/src/xml/helpdesk_team_templates.xml",
    # ],
    'demo': ['data/helpdesk_demo.xml'],
    'application': True,

    'assets': {
        'web._assets_primary_variables': [
            '/product_warranty_axis/static/src/scss/style.scss',
        ],
        'web.assets_qweb': [
            'product_warranty_axis/static/src/xml/helpdesk_team_templates.xml',
        ],
        'web.assets_backend': [
            '/product_warranty_axis/static/src/css/portal_helpdesk.css',
            '/product_warranty_axis/static/src/css/style.css',
            '/product_warranty_axis/static/src/js/helpdesk_dashboard.js',
            '/product_warranty_axis/static/src/js/summary.js',
            '/product_warranty_axis/static/src/js/tours/helpdesk.js',
        ],
        'web.assets_frontend': [
            '/product_warranty_axis/static/src/scss/style.scss',
        ],
    },

    'license': 'OPL-1',
    'price': 90.54,
    'currency': 'USD',
    'support': 'business@axistechnolabs.com',
    'author': 'Axis Technolabs',
    'website': 'http://www.axistechnolabs.com',
    'images': ['static/description/images/Banner-Img.png'],
}
