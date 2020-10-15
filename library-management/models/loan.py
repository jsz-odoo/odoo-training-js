# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta

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
    
    start_date = fields.Date(string="Start Date",
                             default=fields.Date.today)
    
    duration = fields.Integer(string="Loan Duration",
                              default = 1)
    
    end_date = fields.Date(string="End Date",
                           compute="_compute_end_date",
                           inverse="_inverse_end_date",
                           store=True)
    
    late_fee = fields.Float(string="Late Fee",
                            related="asset_ids.fee")
    
    @api.depends("start_date", "duration")
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
                
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue