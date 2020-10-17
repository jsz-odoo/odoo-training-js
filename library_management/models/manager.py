# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Manager(models.Model):
    
    _name = 'library.manager'
    _description = 'Library Manager'
    
    name = fields.Char(text="Name", required=True)
    description = fields.Text(string="Description")