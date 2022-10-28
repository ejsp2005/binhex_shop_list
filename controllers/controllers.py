# -*- coding: utf-8 -*-

from odoo import http

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
            if contacto.partnercat_id:
                partnercat_id = contacto.partnercat_id[0].id
                if partnercat_id not in categorias_id:
                    categorias_id.append(partnercat_id)

                contactdata.update({'partnercat_id': partnercat_id})
            i+=1
            print("ERNESTO_DEBUG " + str(i) + ": " + str(contactdata))
            shop_list.append(contactdata)

        print("ERNESTO_DEBUG: "+str(categorias_id))
        return http.request.render('binhex_shop_list.shops',{
            'contactos': shop_list,
            'categorias': http.request.env['product.public.category'].sudo().browse(categorias_id)
        })
