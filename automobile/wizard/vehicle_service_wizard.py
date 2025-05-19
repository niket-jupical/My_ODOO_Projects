from odoo import models, fields, api

class VehicleServiceWizard(models.TransientModel):
    _name = 'automobile.vehicle.service.wizard'
    _description = 'Vehicle Service Scheduler Wizard'

    vehicle_id = fields.Many2one('automobile.vehicle', string='Vehicle', required=True)
    service_date = fields.Datetime(string='Service Date', required=True)
    notes = fields.Text(string='Service Notes')

    def schedule_service(self):
        """ This method schedules a service for the selected vehicle """
        service_obj = self.env['automobile.vehicle.service']
        service_obj.create({
            'vehicle_id': self.vehicle_id.id,
            'service_date': self.service_date,
            'notes': self.notes
        })
