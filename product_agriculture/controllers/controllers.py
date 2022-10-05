# -*- coding: utf-8 -*-
# from odoo import http


# class ProductAgriculture(http.Controller):
#     @http.route('/product_agriculture/product_agriculture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_agriculture/product_agriculture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_agriculture.listing', {
#             'root': '/product_agriculture/product_agriculture',
#             'objects': http.request.env['product_agriculture.product_agriculture'].search([]),
#         })

#     @http.route('/product_agriculture/product_agriculture/objects/<model("product_agriculture.product_agriculture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_agriculture.object', {
#             'object': obj
#         })
