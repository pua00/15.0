import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.patient_card'
    _description = 'Patient card'

    name = fields.Char()

