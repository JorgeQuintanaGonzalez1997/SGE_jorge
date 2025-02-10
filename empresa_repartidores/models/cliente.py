# -*- coding: utf-8 -*-

from odoo import models, fields, api

#De cada client s’emmagatzema el DNI, nom, cognoms i telèfon.
class cliente(models.Model):
    _name = 'empresa.cliente'
    _description = 'empresa_repartidores.empresa_repartidores'

    nombre = fields.Char()
    apellidos = fields.Char()
    dni = fields.Char()
    telefono = fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100