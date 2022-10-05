# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerAgriculture(http.Controller):
#     @http.route('/partner_agriculture/partner_agriculture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_agriculture/partner_agriculture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_agriculture.listing', {
#             'root': '/partner_agriculture/partner_agriculture',
#             'objects': http.request.env['partner_agriculture.partner_agriculture'].search([]),
#         })

#     @http.route('/partner_agriculture/partner_agriculture/objects/<model("partner_agriculture.partner_agriculture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_agriculture.object', {
#             'object': obj
#         })
