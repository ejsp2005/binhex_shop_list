# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    partnercat_id = fields.Many2one(
        "product.public.category", 
        "name"
    )

