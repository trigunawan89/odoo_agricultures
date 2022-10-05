# -*- coding: utf-8 -*-
# from odoo import http


# class MrpAgriculture(http.Controller):
#     @http.route('/mrp_agriculture/mrp_agriculture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_agriculture/mrp_agriculture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_agriculture.listing', {
#             'root': '/mrp_agriculture/mrp_agriculture',
#             'objects': http.request.env['mrp_agriculture.mrp_agriculture'].search([]),
#         })

#     @http.route('/mrp_agriculture/mrp_agriculture/objects/<model("mrp_agriculture.mrp_agriculture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_agriculture.object', {
#             'object': obj
#         })
