import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class PersonalDoctorHistory(models.Model):
    _name = 'hr_hospital.personal_doctor_history'
    _description = 'Personal doctor history'

    change_date = fields.Date(string='Date of change', index=True, required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', 'Doctor', index=True, ondelete='cascade', required=True)
    patient_id = fields.Many2one('hr_hospital.patient', 'Patient', index=True, ondelete='cascade', required=True)
    active = fields.Boolean(default=True)

