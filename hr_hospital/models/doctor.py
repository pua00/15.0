import logging

from odoo import fields, models
from . import person

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'
    _inherit = {'hr_hospital.person': 'person_id'}

    person_id = fields.Many2one(comodel_name='hr_hospital.person')
    profession = fields.Char(string='Profession', required=True)
