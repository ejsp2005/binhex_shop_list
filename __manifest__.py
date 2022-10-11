# -*- coding: utf-8 -*-
{
    'name': "binhex_shop_list",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Binhex",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'static/src/xml/shops.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Se elimino la dependencia 'maps' que no es necesaria
}
