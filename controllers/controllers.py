# -*- coding: utf-8 -*-

from odoo import http

class BinhexShopList(http.Controller):
     @http.route('/contacts', auth='public', website=True)
     def index(self, **kw):
        contactos = http.request.env['res.partner'].sudo().search([('partnercat_id',"!=", False)])
        categorias_id = []
        shop_list = []

        for contacto in contactos:
            contactdata = {
                'id': contacto.id,
                'name': contacto.name,
                'phone': contacto.phone,
                'job': contacto.function
            }
            if contacto.partnercat_id:
                partnercat_id = contacto.partnercat_id[0].id
                if partnercat_id not in categorias_id:
                    categorias_id.append(partnercat_id)

                contactdata.update({'partnercat_id': partnercat_id})
            shop_list.append(contactdata)

        return http.request.render('binhex_shop_list.shops',{
            'contactos': shop_list,
            'categorias': http.request.env['product.public.category'].sudo().browse(categorias_id)
        })
