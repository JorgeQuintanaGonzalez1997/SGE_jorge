from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PrestarComic(models.Model):
    _name ='biblioteca.prestar'
    _description = "Para gestionar los cómics prestados"
    
    nombre = fields.Char(string="Comic")
    fechaInicio = fields.Date(string="Fecha de inicio", default=fields.Date.today)
    fechaFinal = fields.Date(string="Fecha de préstamo", required=True)

    @api.constrains('fechaInicio', 'fechaFinal')
    def _check_dates(self):
        # Asegurarse de que la fecha de inicio no esté en el futuro
        if self.fechaInicio > date.today():
            raise ValidationError("La fecha de inicio no puede ser posterior al día de hoy.")
        
        # Asegurarse de que la fecha de devolución no esté en el pasado
        if self.fechaFinal < date.today():
            raise ValidationError("La fecha prevista de devolución no puede ser anterior al día de hoy.")
        
        # Asegurarse de que la fecha de devolución no sea anterior a la fecha de inicio
        if self.fechaFinal < self.fechaInicio:
            raise ValidationError("La fecha de devolución no puede ser anterior a la fecha de inicio del préstamo.")

