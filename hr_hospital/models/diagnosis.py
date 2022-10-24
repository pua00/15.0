import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
