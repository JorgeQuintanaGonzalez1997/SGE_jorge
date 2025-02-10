
from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'ciclo_superior.ciclo_superior'

    nombre = fields.Char()
    id_modulo=fields.Many2many("instituto.modulo")
    
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100