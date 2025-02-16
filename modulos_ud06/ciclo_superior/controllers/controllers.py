# -*- coding: utf-8 -*-
# from odoo import http


# class CicloSuperior(http.Controller):
#     @http.route('/ciclo_superior/ciclo_superior', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ciclo_superior/ciclo_superior/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ciclo_superior.listing', {
#             'root': '/ciclo_superior/ciclo_superior',
#             'objects': http.request.env['ciclo_superior.ciclo_superior'].search([]),
#         })

#     @http.route('/ciclo_superior/ciclo_superior/objects/<model("ciclo_superior.ciclo_superior"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ciclo_superior.object', {
#             'object': obj
#         })

