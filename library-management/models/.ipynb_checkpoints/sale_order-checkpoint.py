# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    loan_id = fields.Many2one(comodel_name="library.loan",
                              string="Related Loan",
                              ondelete="set null")
    
    patron_id = fields.Many2one(string="Patron",
                                related="loan_id.patron_id")
    
    asset_ids = fields.Many2many(string="Books",
                                 related="loan_id.asset_ids")
    
    is_taxcloud = fields.Boolean(default=False)
    
    is_taxcloud_configured = fields.Boolean(default=False)