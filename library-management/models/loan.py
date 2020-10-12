# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Loan(models.Model):
    
    _name = "library.loan"
    _description = "Library Loan"
    
    description = fields.Text(default="""
        A library loan
    """)
    
    active = fields.Boolean(string="Is Active", default=True, required=True)
    
    asset_ids = fields.Many2many(comodel_name="library.book", string="Books")
    
    patron_id = fields.Many2one(comodel_name="library.patron", 
                                string="Patron",
                                ondelete="cascade")
    
    name = fields.Char(string="Loan", required=True)