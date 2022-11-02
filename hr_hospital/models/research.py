import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Research(models.Model):
    _name = 'hr_hospital.research'
    _description = 'Research'

    patient_id = fields.Many2one(comodel_name='hr_hospital.patient',
                                 string='Patient',
                                 required=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True)
    type_of_research_id = fields.Many2one(comodel_name='hr_hospital.type_of_research',
                                          string='Research',
                                          required=True)
    type_of_sample_id = fields.Many2one(comodel_name='hr_hospital.type_of_sample',
                                        string='Samples',)
    conclusion = fields.Text(string='Conclusion')
    visit_doctor_id = fields.Many2one(comodel_name='hr_hospital.visit_doctor',
                                      string='Visit of doctor',
                                      required=True)
    active = fields.Boolean(default=True)
