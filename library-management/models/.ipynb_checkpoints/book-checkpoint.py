# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Library Book'
    
    title = fields.Text(string="Title", required=True)
    isbn = fields.Char(string="ISBN", 
                       required=True,
                       help="The International Standard Book Number consisting of up to 13 digits (formerly 10)",
                       size=13)
    page_length = fields.Integer(string="Page Length")
    loaned_out = fields.Boolean(default=False)