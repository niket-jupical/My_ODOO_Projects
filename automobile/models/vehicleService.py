from odoo import models,fields


class VehicleService(models.Model):
    _name='automobile.vehicle.service'
    _description='Vehicle Service Record'
    
    service_date = fields.Date(string='Service Date')
    description = fields.Text(string='Service Description')
    vehicle_id = fields.Many2one('automobile.vehicle',string='Vehicle')
    