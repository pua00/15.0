import logging

from odoo import api, fields, models
from datetime import date, datetime
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
    personal_doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', string='Person doctor')

    @api.depends('date_of_birth')
    def _computed_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    def write(self, vals):
        patient = super(Patient, self).write(vals)
        if 'personal_doctor_id' in vals:
            doc_history = {'change_date': datetime.now(),
                           'patient_id': self.id,
                           'doctor_id': self.personal_doctor_id.id}
            self.env['hr_hospital.personal_doctor_history'].create(doc_history)

        return patient
