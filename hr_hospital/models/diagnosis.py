import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
