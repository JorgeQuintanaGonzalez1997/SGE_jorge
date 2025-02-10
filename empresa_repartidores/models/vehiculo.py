# -*- coding: utf-8 -*-

from odoo import models, fields, api

#La nostra empresa té empleats que poden o no tindre carnet de ciclomotor o furgoneta. A
#banda d’una foto i dades típiques de les persones (nom, cognom, DNI i telèfon).
class vehiculo(models.Model):
    _name = 'empresa.vehiculo'
    _description = 'empresa_repartidores.empresa_repartidores'

    tipo= fields.Selection([
        ('bicicleta', 'Bicicleta'),
        ('motocicleta', 'Motocicleta'),
        ('furgoneta', 'Furgoneta'),
        # Agregar más tipos según sea necesario
    ], string='Tipo de Vehículo')
    foto = fields.Binary(string='Foto', attachment=True)
    matricula = fields.Char()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100