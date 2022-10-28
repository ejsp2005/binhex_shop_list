# -*- coding: utf-8 -*-
{
    'name': "Binhex Shop List",

    'summary': """
        Módulo que crea una página web con los contactos del Odoo, separados por las categorías asignadas.
    """,

    'description': """
        Módulo que: 
        - Utiliza los contactos de ejemplo de Odoo para crear una lista de usuarios agrupados por categorías.
    """,

    'author': "Binhex",
    'website': "http://www.binhex.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'static/src/xml/shops.xml',
        'static/src/xml/assets.xml',
        'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    # Se elimino la dependencia 'maps' que no es necesaria
}
