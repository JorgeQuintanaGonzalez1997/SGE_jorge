# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Cada repartiment té un codi autonuméric únic, una data i hora d'inici i una de retorn, a més
#d'una data de recepció, un repartidor, un vehicle, els kilòmetres del repartiment, el pes(kg)
#i volum del paquet, observacions, estat de l'entrega (no ha eixit, de camí o entregada), el
#client emissor i les dades del receptor.
class reparto(models.Model):
    _name = 'empresa.reparto'
    _description = 'Repartiment'
    _order = 'urgencia,data_recepcio'

    # Codi autonumèric únic
    codi = fields.Char(string='Codi Repartiment', required=True, readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('repartiment.sequence'))

    # Dates
    data_inici = fields.Datetime(string='Data d\'Inici', required=True)
    data_retorn = fields.Datetime(string='Data de Retorn', required=True)
    data_recepcio = fields.Date(string='Data de Recepció')

    # Relación con el repartidor y el vehículo
    repartidor_id = fields.Many2one('empresa.empleado', string='Repartidor', required=True)
    vehicle_id = fields.Many2one('empresa.vehiculo', string='Vehicle', required=True)

    # Kilòmetres, pes i volum
    kilometres = fields.Float(string='Kilòmetres', required=True)
    pes = fields.Float(string='Pes (kg)', required=True)
    volum = fields.Float(string='Volum (m3)', required=True)

    # Observacions
    observacions = fields.Text(string='Observacions')

    # Estat de l'entrega
    estat_entrega = fields.Selection([
        ('no_eixit', 'No ha eixit'),
        ('de_camí', 'De camí'),
        ('entregada', 'Entregada')
    ], string='Estat de l\'entrega', default='no_eixit', required=True)
    urgencia = fields.Selection([
        ('organs_humans', 'Òrgans Humans'),
        ('aliments_refrigerats', 'Aliments Refrigerats'),
        ('aliments', 'Aliments'),
        ('alta_prioritat', 'Alta Prioritat'),
        ('baixa_prioritat', 'Baixa Prioritat'),
    ], string='Urgència', default='baixa_prioritat', required=True)

    # Relación con el client emissor i receptor
    client_emissor_id = fields.Many2one('empresa.cliente', string='Client Emissor', required=True)
    client_receptor_id = fields.Many2one('empresa.cliente', string='Client Receptor', required=True)
    repartidor_id = fields.Many2one('empresa.empleado', string='Repartidor', required=True)
    @api.model
    def create(self, vals):
        # Verificar que el empleado tiene carnet antes de crear el registro de reparto
        repartidor = self.env['empresa.empleado'].browse(vals.get('repartidor_id'))
        if not repartidor.carnet:
            raise Exception("El repartidor no tiene un carnet asignado. No se puede crear el repartimiento.")
        
        # Si el carnet está presente, continuar con la creación del registro
        return super(reparto, self).create(vals)
    @api.constrains('kilometres', 'vehicle_id')
    def _check_bicycle_distance(self):
        for record in self:
            # Verificar si el vehículo es una bicicleta
            if record.vehicle_id.tipo == 'bicicleta' and record.kilometres > 10:
                raise Exception("Els repartiments de més de 10 km no es poden fer en bicicleta.")
    @api.constrains('kilometres', 'vehicle_id')
    def _check_furgoneta_distance(self):
        for record in self:
            # Verificar si el vehículo es una bicicleta
            if record.vehicle_id.tipo == 'furgoneta' and record.kilometres < 1:
                raise Exception("Els repartiments de menos de 1 km no es poden fer en furgoneta.")
