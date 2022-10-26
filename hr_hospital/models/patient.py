import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Full name', required=True)
    gender = fields.Selection(string='Gender', selection=[('male', "Male"), ('femail', "Femail")], default='male', required=True)
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age of patient')
    passport_date = fields.Char(string='Passport date')
    contact_person = fields.Char(string='Person for contact')
