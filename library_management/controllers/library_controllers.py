# -*- coding: utf-8 -*-

from odoo import http

class Library(http.Controller):
    
    @http.route('/library/', auth='public', website=True)
    def index(self, **kw):
        
        return "Hello world"

    
    @http.route('/library/assets/', auth='public', website=True)
    def assets(self, **kw):
        
        assets = http.request.env['library.book'].search([])
        
        return http.request.render('library_management.asset_website', {
            'assets': assets,
        })
                
                
    @http.route('/library/<model("library.loan"):loan>/', auth='public', website=True)
    def loan(self, loan):
        
        return http.request.render('library_management.loan_website', {
            'loan': loan,
        })