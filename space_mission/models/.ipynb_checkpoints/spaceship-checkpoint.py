# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'spacemission.spaceship'
    _description = 'Spaceship'
    
    name = fields.Char(string='Spaceship', required=True)
    description = fields.Text(string='A Spaceship')
    
    dimensions = fields.Char(string='dimensions', default='40 x 20')
    fuel_type = fields.Char(string='Fuel Type')
    number_of_passengers = fields.Integer(string='Number of Passengers', default=10)
    ship_type = fields.Selection(string='Ship Type',
                                 selection=[('shuttle', 'Shuttle'),
                                            ('freighter', 'Freighter'),
                                            ('fighter', 'Fighter'),
                                            ('medical', 'Medical')],
                                 copy=False)
    active = fields.Boolean(string='Active', default=True)