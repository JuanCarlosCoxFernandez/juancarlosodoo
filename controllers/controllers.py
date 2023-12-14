# -*- coding: utf-8 -*-
# from odoo import http


# class Juancarlosodoo(http.Controller):
#     @http.route('/juancarlosodoo/juancarlosodoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/juancarlosodoo/juancarlosodoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('juancarlosodoo.listing', {
#             'root': '/juancarlosodoo/juancarlosodoo',
#             'objects': http.request.env['juancarlosodoo.juancarlosodoo'].search([]),
#         })

#     @http.route('/juancarlosodoo/juancarlosodoo/objects/<model("juancarlosodoo.juancarlosodoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('juancarlosodoo.object', {
#             'object': obj
#         })
