import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ScheduleOfDoctor(models.Model):
    _name = 'hr_hospital.schedule_of_doctor'
    _description = 'Schedule of Doctor'

    name = fields.Char(string='Schedule of Doctor', compute='_computed_name')
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', string='Doctor', required=True, index=True)
    visit_date = fields.Date(string='Date for visit', required=True)
    visit_from_date = fields.Datetime(string='Visit from', required=True)
    visit_to_date = fields.Datetime(string='Visit to', required=True)
    active = fields.Boolean(default=True)

    def _computed_name(self):
        for rec in self:
            rec.name = 'Doc schedule'
            # rec.name = rec.doctor_id
            # rec.name += ' [' + rec.visit_from_date + ']'
            # rec.name += ' - [' + rec.visit_to_date + ']'
