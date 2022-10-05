# -*- coding: utf-8 -*-
# from odoo import http


# class ReportAgriculture(http.Controller):
#     @http.route('/report_agriculture/report_agriculture/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_agriculture/report_agriculture/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_agriculture.listing', {
#             'root': '/report_agriculture/report_agriculture',
#             'objects': http.request.env['report_agriculture.report_agriculture'].search([]),
#         })

#     @http.route('/report_agriculture/report_agriculture/objects/<model("report_agriculture.report_agriculture"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_agriculture.object', {
#             'object': obj
#         })
