import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(string='Disease', required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', 'Doctor', help='Select your doctor', required=True, create=False)
    patient_id = fields.Many2one('hr_hospital.patient', 'Patient', help='Select your patient', required=True)
    prescribe_treatment = fields.Text(string='Prescribe treatment')
    date_of_diagnosis = fields.Date(string='Date of diagnosis', default=fields.Date.today, required=True)
