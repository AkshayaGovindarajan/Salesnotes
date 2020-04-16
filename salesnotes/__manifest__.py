# -*- coding: utf-8 -*-
{
    'name': "Salesnotes",

    'summary': """
        Log salesnotes""",

    'description': """
       Salesnotes for SalesPerson
    """,

    'author': "PQI",
    'website': "http://www.gagesite.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sales_notes_view.xml',        
    ],
    'application': False,
    'installable': True,
    'auto_install': False
}
