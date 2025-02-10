# -*- coding: utf-8 -*-

from odoo import models, fields, api

#La nostra empresa té empleats que poden o no tindre carnet de ciclomotor o furgoneta. A
#banda d’una foto i dades típiques de les persones (nom, cognom, DNI i telèfon).
class empleado(models.Model):
    _name = 'empresa.empleado'
    _description = 'empresa_repartidores.empresa_repartidores'

    nombre = fields.Char()
    foto = fields.Binary(string='Foto', attachment=True)
    carnet = fields.Selection(
        [('ciclomotor', 'Carnet ciclomotor'), 
         ('furgoneta', 'Carnet furgoneta')],
        string='Elige una opción',
        required=True,
        default='ciclomotor'  # Opcional: valor por defecto
    )
    description = fields.Text()
    repartos_ids = fields.One2many('repartiment', 'repartidor_id', string='Repartiments')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100