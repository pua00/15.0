import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(string='Diagnosis',
                       required=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                help='Select your doctor',
                                required=True,
                                create=False)
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient',
                                 string='Patient',
                                 help='Select your patient',
                                 required=True)
    prescribe_treatment = fields.Text(string='Prescribe treatment')
    date_of_diagnosis = fields.Date(string='Date of diagnosis',
                                    default=fields.Date.today,
                                    required=True)
    is_intern = fields.Boolean(string='This is doctor-intern',
                               related='doctor_id.is_intern')
    doctor_mentor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                       string='Doctor-mentor',
                                       related='doctor_id.doctor_mentor_id')
    comment_doctor_mentor = fields.Text(string='Comment doctor-mentor',
                                        domain=[('is_intern', "=", False)])
    # research_ids = fields.One2many('hr_hospital.research',
    #                                inverse_name='patient_id',
    #                                 string='Researches')
    visit_doctor_id = fields.Many2one(comodel_name='hr_hospital.visit_doctor',
                                      string='Visit doctor',
                                      help='Select your visit doctor',
                                      required=True)
    active = fields.Boolean(default=True)
