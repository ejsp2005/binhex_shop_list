# -*- coding: utf-8 -*-
# import logging
# _logger = logging.getLogger(__name__)

# from odoo.addons.portal.controllers.web import Home
# from asyncio.windows_events import NULL
from odoo import http
# from odoo.http import request

class BinhexShopList(http.Controller):
     @http.route('/contacts', auth='public', website=True)
     def index(self, **kw):
        contactos = http.request.env['res.partner'].sudo().search([('partnercat_id',"!=", False)])
        categorias_id = []
        shop_list = []

        i=0
        for contacto in contactos:
            contactdata = {
                'id': contacto.id,
                'name': contacto.name,
                'phone': contacto.phone,
                'mobile': contacto.mobile
            }
            if contacto.function:
                if contacto.partnercat_id not in categorias_id:
                    categorias_id.append(contacto.partnercat_id)

                contactdata.update({'function': contacto.partnercat_id})
            i+=1
            # print("ERNESTO_DEBUG " + str(i) + ": " + str(contactdata))
            shop_list.append(contactdata)

        print("ERNESTO_DEBUG: "+str(categorias_id))
        return http.request.render('binhex_shop_list.shops',{
            'contactos': shop_list,
            'categorias': http.request.env['product.public.category'].sudo().browse(categorias_id)
        })
