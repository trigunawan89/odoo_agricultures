# -*- coding: utf-8 -*-
# from odoo import http


# class OdooAgriculture(http.Controller):
#     @http.route('/odoo_agriculture/odoo_agriculture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_agriculture/odoo_agriculture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_agriculture.listing', {
#             'root': '/odoo_agriculture/odoo_agriculture',
#             'objects': http.request.env['odoo_agriculture.odoo_agriculture'].search([]),
#         })

#     @http.route('/odoo_agriculture/odoo_agriculture/objects/<model("odoo_agriculture.odoo_agriculture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_agriculture.object', {
#             'object': obj
#         })
