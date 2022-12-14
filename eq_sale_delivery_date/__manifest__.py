# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

{
    'name' : 'Sale Delivery by Date',
    'category': 'Sale',
    'version': '14.0.1.0',
    'author': 'Equick ERP',
    'description': """
        This Module allows to create delivery order based on delivery date in sale order line.
        * Allows you to create delivery order based on delivey date from sale order lines.
        * Allows you to change delivery date for multiple product at a single time.
    """,
    'summary': """ This Module allows to create delivery order based on delivery date in sale order line. sale order delivery by date | delivery order by date | sale by delivery date """,
    'depends' : ['base', 'sale_management', 'sale_stock'],
    'price': 20,
    'currency': 'EUR',
    'license': 'OPL-1',
    'website': "",
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
    ],
    'demo': [],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
