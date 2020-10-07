# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Patron(models.Model):
    
    _name = 'library.patron'
    _description = 'Library Patron'