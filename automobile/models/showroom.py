from odoo import models,fields

class Showroom(models.Model):
    _name='automobile.showroom'
    _description='Automobile Showroom'
    
    name=fields.Char(string='Showroom Name', required=True)
    location=fields.Char(string='Location')
    vehicle_ids=fields.Many2many('automobile.vehicle',string='Vehicles Available')