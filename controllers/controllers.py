# -*- coding: utf-8 -*-
from odoo import http
import logging
_logger = logging.getLogger(__name__)

from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request

class BinhexShopList(http.Controller):
     @http.route('/shops', auth='public',website=True)
     def index(self, **kw):
         shops = http.request.env['res.partner'].sudo().search([('planta_id','!=',False)])
         categories_ids = []
         shops_list = []

         for s in shops:
             t_aux = {
                'id': s.id,
                'name': s.name,
                'horario': s.horario,
                'planta_id': s.planta_id,
                'local_id': s.local_id,
                'phone': s.phone,
                'mobile': s.mobile,
             }
             if s.categoria:
                 if s.categoria[0].id not in categories_ids:
                     categories_ids.append(s.categoria[0].id)
                     t_aux.update({'categoria': s.categoria[0].id})
                 else:
                     t_aux.update({'categoria': s.categoria[0].id})
             _logger.info("DEBBUG "+str(t_aux))
             shops_list.append(t_aux)

         return http.request.render('binhex_shop_list.shops',{
            'shops': shops_list,
            'categories': http.request.env['product.public.category'].sudo().browse(categories_ids)
         })
