import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ScheduleOfDoctor(models.Model):
    _name = 'hr_hospital.schedule_of_doctor'
    _description = 'Schedule of Doctor'

    name = fields.Char(string='Schedule of Doctor', compute='_computed_name')
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', string='Doctor',
                                required=True, index=True)
    visit_date = fields.Date(string='Date', required=True)
    visit_start_datetime = fields.Datetime(string='Visit start from', required=True)
    active = fields.Boolean(default=True)

    def _computed_name(self):
        for rec in self:
            rec.name = str(rec.doctor_id.name) + ' - [' + str(rec.visit_start_datetime) + ']'

    @api.onchange('visit_start_datetime, doctor_id')
    def _compute_visit_start_datetime(self):
        #It bad works
        sizes = self.search([('visit_start_datetime', '=', self.visit_start_datetime),
                             ('doctor_id', '=', self.doctor_id.id)])
        print('sizes---', len(sizes))
        if len(sizes) != 0:
            self.visit_start_datetime = ""
