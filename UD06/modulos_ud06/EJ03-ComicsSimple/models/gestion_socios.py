from datetime import timedelta
from odoo import fields,api,models
from odoo.exceptions import ValidationError


class GestionarSocios(models.Model):
    _name='biblioteca.socio'
    _description='Gestion de socios'

    id = fields.Integer(string="id",required=True)
    nombre = fields.Char(string="nombre")
    apellido = fields.Char(string="apellido")