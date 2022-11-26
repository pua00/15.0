import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Shelf(models.Model):
    _name = 'pua_cartridge.shelf'
    _description = 'Shelf'

    name = fields.Char(string='Shelf`s name',
                       required=True)
    is_shelfOfUser = fields.Boolean(string='Shelf of engineer',
                                    default=False)
    engineer_id = fields.Many2one(comodel_name='pua_cartridge.engineer',
                                  string='Engineer')
    active = fields.Boolean(default=True)
