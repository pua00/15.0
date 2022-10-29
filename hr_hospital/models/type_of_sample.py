import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class TypeOfSample(models.Model):
    _name = 'hr_hospital.type_of_sample'
    _description = 'Type of sample'

    name = fields.Char(string='Type of sample', required=True)
    active = fields.Boolean(default=True)
