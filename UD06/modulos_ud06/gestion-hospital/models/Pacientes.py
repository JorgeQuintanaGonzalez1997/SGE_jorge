# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pacientes(models.Model):
    _name = 'hospital.paciente'
    _description = 'gestion-hospital.gestion-hospital'

    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    sintomas = fields.Char(string="Sintomas")
    id_medico=fields.One2many("hospital.medico","id_paciente")
    diagnostico_id=fields.One2many("hospital.diagnostico","id_paciente")
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

