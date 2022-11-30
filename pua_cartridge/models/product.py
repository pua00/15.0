import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Product(models.Model):
    _inherit = 'product.product'

    is_for_repair_cartridge = fields.Boolean(
        string='This product for repair cartridge')
