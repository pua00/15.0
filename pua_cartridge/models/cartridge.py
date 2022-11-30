import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Cartridge(models.Model):
    _name = 'pua_cartridge.cartridge'
    _description = 'Cartridge'

    name = fields.Char(string='Name Cartridge',
                       required=True)
    barcode = fields.Char(string='Individual barcode')
    type_of_cartridge_id = fields.Many2one(
        comodel_name='pua_cartridge.type_of_cartridge',
        string='Type of cartridge')
    partner_id = fields.Many2one(comodel_name='res.partner',
                                 string='Partner')
    active = fields.Boolean(default=True)

    @api.onchange('type_of_cartridge_id')
    def onchange_type_of_cartridge_id(self):
        if self.type_of_cartridge_id:
            self.name = self.type_of_cartridge_id.name
        else:
            self.name = False
