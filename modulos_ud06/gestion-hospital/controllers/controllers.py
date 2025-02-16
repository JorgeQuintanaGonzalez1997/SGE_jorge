# -*- coding: utf-8 -*-
# from odoo import http


# class Gestion-hospital(http.Controller):
#     @http.route('/gestion-hospital/gestion-hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion-hospital/gestion-hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion-hospital.listing', {
#             'root': '/gestion-hospital/gestion-hospital',
#             'objects': http.request.env['gestion-hospital.gestion-hospital'].search([]),
#         })

#     @http.route('/gestion-hospital/gestion-hospital/objects/<model("gestion-hospital.gestion-hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion-hospital.object', {
#             'object': obj
#         })

