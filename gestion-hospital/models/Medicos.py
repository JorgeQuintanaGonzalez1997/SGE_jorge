from odoo import models, fields, api



class Medicos(models.Model):
    _name = 'hospital.medico'
    _description = 'gestion-hospital.gestion-hospital'

    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    numeroColegiado = fields.Integer(string="Número de colegiado")
    id_paciente=fields.Many2one("hospital.paciente")
    id_diagnostico=fields.One2many("hospital.diagnostico","id_medico")
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100