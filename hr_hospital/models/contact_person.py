import logging

from odoo import fields, models
from . import person

_logger = logging.getLogger(__name__)


class ContactPerson(models.Model):
    _name = 'hr_hospital.contact_person'
    _description = 'Contact person'
    _inherit = {'hr_hospital.person': 'person_id'}

    person_id = fields.Many2one(comodel_name='hr_hospital.person')