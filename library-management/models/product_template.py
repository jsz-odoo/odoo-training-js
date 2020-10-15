# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    is_loan_product = fields.Boolean(string="Use as Loan Product",
                                     help="Check this box to use this as a Product for Loan",
                                     default=False)