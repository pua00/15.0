import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    type_of_customer = fields.Selection(
        selection=[('regular_customer', "Regular customer"),
                   ('temporary_customer', "Temporary customer")],
        default='temporary_customer')
