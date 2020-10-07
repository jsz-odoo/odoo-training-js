# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Patron(models.Model):
    
    _name = 'library.patron'
    _description = 'Library Patron'
    
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required="True")
    email = fields.Char(string="Email Address", required=True)
    phone_number = fields.Char(string="Phone Number")