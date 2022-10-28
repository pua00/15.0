import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr_hospital.visit_doctor'
    _description = 'Visit doctor'

    visit_time = fields.Datetime(string='Visit time', required=True, index=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', string='Doctor', required=True, index=True)
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient', string='Patient', required=True, index=True)
    diagnose = fields.Text(string='Diagnose of patient')
    recommendation = fields.Text(string='Recommendation')
    active = fields.Boolean(default=True)
