import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class TypeOfCartridge(models.Model):
    _name = 'pua_cartridge.type_of_cartridge'
    _description = 'Type of Cartridge'

    name = fields.Char(string='Type of Cartridge',
                       required=True)
    active = fields.Boolean(default=True)
