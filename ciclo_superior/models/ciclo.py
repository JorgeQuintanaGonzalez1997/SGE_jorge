
from odoo import models, fields, api


class Ciclo(models.Model):
    _name = 'instituto.ciclo'
    _description = 'ciclo_superior.ciclo_superior'

    nombre = fields.Char()
    id_modulos=fields.One2many("instituto.modulo","id_ciclo")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100