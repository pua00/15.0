import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Research(models.Model):
    _name = 'hr_hospital.research'
    _description = 'Research'

    research_date = fields.Datetime(string='Date of research',
                                    default=fields.Date.today,
                                    index=True,
                                    required=True)
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient',
                                 string='Patient',
                                 required=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True)
    type_of_research_id = fields.Many2one(
        comodel_name='hr_hospital.type_of_research',
        string='Research',
        required=True)
    type_of_sample_id = fields.Many2one(
        comodel_name='hr_hospital.type_of_sample',
        string='Samples', )
    conclusion = fields.Text()

    active = fields.Boolean(default=True)

    def name_get(self):
        return [(tag.id, 'Research {}: {} = > {}'
                 .format(self.research_date or "",
                         tag.doctor_id.name or "",
                         tag.patient_id.name or "")) for tag in self]
