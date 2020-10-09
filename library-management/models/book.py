# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Book(models.Model):
    
    _name = 'library.book'
    _description = 'Library Book'
    
    name = fields.Char(string="Name", default="Book")
    title = fields.Text(string="Title", required=True)
    isbn = fields.Char(string="ISBN", 
                       required=True,
                       help="The International Standard Book Number consisting of up to 13 digits (formerly 10)",
                       size=13)
    page_length = fields.Integer(string="Pages", default=0)
    loaned_out = fields.Boolean(string="Loaned", default=False)
    
    @api.constrains("isbn")
    def _check_isbn_length(self):
        for record in self:
            if len(record.isbn) < 10:
                raise ValidationError("The ISBN has to be between 10 and 13 digits in length, current length is: %s" % len(record.isbn))
                
    
    @api.onchange("page_length")
    def _onchange_page_length(self):
        if self.page_length < 0:
            raise UserError("Number of pages cannot be negative.")
    