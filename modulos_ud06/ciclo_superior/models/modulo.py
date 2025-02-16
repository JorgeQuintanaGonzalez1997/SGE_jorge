
from odoo import models, fields, api


class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'ciclo_superior.ciclo_superior'

    nombre = fields.Char()
    id_ciclo=fields.Many2one("instituto.ciclo")
    id_alumno=fields.Many2many("instituto.alumno")
    id_profesor=fields.Many2many("instituto.profesor")
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100