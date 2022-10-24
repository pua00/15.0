import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'

    name = fields.Char()
    first_name = fields.Char()
    sur_name = fields.Char()
