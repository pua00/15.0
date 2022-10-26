import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Full name', required=True)
    profession = fields.Char(string='Profession', required=True)
