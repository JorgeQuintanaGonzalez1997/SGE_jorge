
from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'ciclo_superior.ciclo_superior'

    nombre = fields.Char()
    id_modelo=fields.Many2many("instituto.modelo")
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100