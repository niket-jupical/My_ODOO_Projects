from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Parts(models.Model):
    _name = 'automobile.parts'
    _description = 'Automobile Parts'

    name = fields.Char(string='Part Name', required=True)
    part_number = fields.Char(string='Series')
    price = fields.Float(string='Price')
    part_manufacturer = fields.Char(string='Manufacturer Name')

    # CRUD Operations

    def create_part(self, name, part_number, price, manufacturer):
        """
        Create a new part record.
        """
        part_values = {
            'name': name,
            'part_number': part_number,
            'price': price,
            'part_manufacturer': manufacturer
        }
        new_part = self.env['automobile.parts'].create(part_values)
        _logger.info(f"New Part Created: {new_part.name} with ID: {new_part.id}")
        return new_part

    def read_parts(self, domain=None):
        """
        Fetch parts based on a search domain.
        If no domain is specified, fetches all parts.
        """
        if domain is None:
            domain = []
        
        parts = self.env['automobile.parts'].search(domain)
        for part in parts:
            _logger.info(f"Part Found: {part.name} - Series: {part.part_number} - Price: {part.price}")
        return parts

    def update_part(self, part_id, values):
        """
        Update the part details.
        """
        part = self.env['automobile.parts'].browse(part_id)
        if part.exists():
            part.write(values)
            _logger.info(f"Part Updated: {part.name} - New Values: {values}")
            return True
        else:
            _logger.error(f"No part found with ID: {part_id}")
            return False

    def delete_part(self, part_id):
        """
        Delete a part from the database.
        """
        part = self.env['automobile.parts'].browse(part_id)
        if part.exists():
            part.unlink()
            _logger.info(f"Part Deleted Successfully: {part_id}")
            return True
        else:
            _logger.error(f"Cannot delete part; ID {part_id} not found.")
            return False

    
    # Button Actions for UI
    def action_update_price(self):
        """
        Button action to increase the price by 100.
        """
        self.write({'price': self.price + 100})
        _logger.info(f"Price updated for Part: {self.name}")

    def action_delete_part(self):
        """
        Button action to delete the part.
        """
        self.unlink()
        _logger.info(f"Part {self.name} deleted from the database")
