# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Patron(models.Model):
    
    _name = 'library.patron'
    _description = 'Library Patron'
    
    first_name = fields.Char(string="First Name", required=True)
    
    last_name = fields.Char(string="Last Name", required="True")
    
    name = fields.Char(compute="_compute_full_name")
    
    email = fields.Char(string="Email Address", required=True)
    
    phone_number = fields.Char(string="Phone Number")
    
    loan_ids = fields.One2many(comodel_name="library.loan", 
                               inverse_name="patron_id",
                               string="Loans")
    
    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for record in self:
            record.name = record.first_name + " " + record.last_name