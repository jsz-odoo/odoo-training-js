# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    
    _name = "library.sale.wizard"
    _description = "Wizard: Loan Order for Library Patrons"
    
    def _default_loan(self):
        return self.env["library.loan"].browse(self._context.get("active_id"))
    
    loan_id = fields.Many2one(comodel_name="library.loan",
                              string="Loan",
                              required=True,
                              default=_default_loan)
    
    loan_asset_ids = fields.Many2many(comodel_name="library.book",
                                      string="Books in Current Loan",
                                      related="loan_id.asset_ids",
                                      help="These are the Books currently on the Loan")
    
    asset_ids = fields.Many2many(comodel_name="library.book",
                                 string="Books for Loan Order")
    
    def create_sale_orders(self):
        
        loan_product_id = self.env["product.product"].search([('is_loan_product','=', True)], limit=1)
        if loan_product_id:
            order_id = self.env['sale.order'].create({
                "patron_id": self.loan_id.patron_id,
                "loan_id": self.loan_id,
                "order_line": [(0,0,{'product_id': loan_product_id.id, 'price_unit': self.loan_id.late_fee})]
            })