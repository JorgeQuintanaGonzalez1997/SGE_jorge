# -*- coding: utf-8 -*-
# from odoo import http


# class EmpresaRepartidores(http.Controller):
#     @http.route('/empresa_repartidores/empresa_repartidores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresa_repartidores/empresa_repartidores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresa_repartidores.listing', {
#             'root': '/empresa_repartidores/empresa_repartidores',
#             'objects': http.request.env['empresa_repartidores.empresa_repartidores'].search([]),
#         })

#     @http.route('/empresa_repartidores/empresa_repartidores/objects/<model("empresa_repartidores.empresa_repartidores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresa_repartidores.object', {
#             'object': obj
#         })

