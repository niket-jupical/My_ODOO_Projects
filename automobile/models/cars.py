from odoo import models,fields

class Automobile(models.Model):
    _name='automobile.vehicle'
    _description='Automobile Cars'
    _order='price asc'  
    
    name = fields.Char(string='Car Name',required=True)
    model = fields.Char(string='Model Name')
    price = fields.Float(string='Price')
    manufacturer = fields.Char(string='Manufacturer')
    color = fields.Char(string='Color')
    available = fields.Boolean(string='Available for Sale',default=True)
    date = fields.Date(string='Default Date',default=fields.Date.today)
    owner_id = fields.Many2one('res.partner', string='Owner')
    manufacturer_id = fields.Many2one('res.partner',string='Manufacturer')
    
    service_ids = fields.One2many('automobile.vehicle.service','vehicle_id',string='Service Records')
    showroom_ids = fields.Many2many('automobile.showroom',string='Showrooms')   