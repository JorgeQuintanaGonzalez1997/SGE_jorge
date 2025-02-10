from odoo import models, fields, api



class Diagnosticos(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'gestion-hospital.gestion-hospital'

    diagnostico=fields.Char(string="Diagnostico")
    id_paciente = fields.Many2one("hospital.paciente")
    id_medico = fields.Many2one("hospital.medico")
    
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100