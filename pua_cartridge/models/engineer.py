import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Engineer(models.Model):
    _name = 'pua_cartridge.engineer'
    _description = 'Engineer'

    name = fields.Char(string='Engineer`s name',
                       required=True)
    active = fields.Boolean(default=True)