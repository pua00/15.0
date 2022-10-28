import logging

from odoo import api, fields, models
from datetime import date
from . import person

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'
    _inherit = {'hr_hospital.person': 'person_id'}

    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age of patient', compute='_computed_age')
    passport_date = fields.Char(string='Passport date')
    contact_person_id = fields.Many2one(comodel_name='hr_hospital.contact_person', string='Person for contact')
    person_id = fields.Many2one(comodel_name='hr_hospital.person')
    personal_doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', compute='_on_change_personal_doctor', string='Person doctor')

    @api.depends('date_of_birth')
    def _computed_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def _on_change_personal_doctor(self):
        print('При зміні персонального лікаря має автоматично створювати запис в історію призначення')

