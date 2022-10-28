import logging

from odoo import api, fields, models
from datetime import date


_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(string='Full name', required=True)
    gender = fields.Selection(string='Gender', selection=[('male', "Male"), ('femail', "Femail")], default='male', required=True)
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age of patient', compute='_computed_age')
    passport_date = fields.Char(string='Passport date')
    contact_person = fields.Char(string='Person for contact')

    @api.depends('date_of_birth')
    def _computed_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
