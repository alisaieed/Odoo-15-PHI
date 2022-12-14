# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Print Journal Entries Report in Odoo',
    'version': '15.0.0.0',
    'category': 'Account',
    'license': 'OPL-1',
    'summary': 'Allow to print pdf report of Journal Entries.',
    'description': """
    Allow to print pdf report of Journal Entries.
    journal entry
    print journal entry 
    journal entries
    print journal entry reports
    account journal entry reports
    journal reports
    account entry reports

    
""",
    'price': 000,
    'currency': 'EUR',
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.in',
    'depends': ['base','account', 'sale', 'purchase'],
    'data': [
            'report/report_journal_entries.xml',
            'report/report_journal_entries_view.xml',
	    'report/report_fitness_invoice.xml',
	    'report/report_invoice_lhc.xml',
	    'report/report_sale_order_fhl.xml',
	    'report/report_sale_order_lhcl.xml',
	    'report/report_purchase_order_fhl.xml',
	    'report/report_purchase_order_lhcl.xml',
    ],
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/qehLT4WOWPs',
    "images":["static/description/Banner.png"],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
