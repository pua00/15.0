import logging

from datetime import datetime, timedelta
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class CreateDoctorScheduleWizard(models.TransientModel):
    _name = 'create_doctor_schedule_wizard'
    _description = _('Create doctor schedule wizard')

    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True)
    week_type = fields.Selection(string='Type of week',
                                 selection=[('first', "First"),
                                            ('second', "Second")],
                                 default='first', required=True)
    start_week_day = fields.Date(string='Week start',
                                 required=True)
    finish_week_day = fields.Date(string='Week finish',
                                  required=True)
    time_start_job = fields.Integer(string='Time start job',
                                    required=True,
                                    default=6)
    time_finish_job = fields.Integer(string='Time finish job',
                                     required=True,
                                     default=12)
    interval_for_visit = fields.Integer(string='Interval for visit',
                                        required=True,
                                        default=15)

    @api.onchange('week_type')
    def _change_time_for_week_type(self):
        if self.week_type == 'first':
            self.time_start_job = 6
            self.time_finish_job = 12
        if self.week_type == 'second':
            self.time_start_job = 12
            self.time_finish_job = 18

    def action_start_wizard(self):

        if not self.start_week_day < self.finish_week_day:
            raise UserError(_('Start day must be big then finish day'))
        if not self.time_start_job < self.time_finish_job:
            raise UserError(_('Start time must be big then finish time'))
        if self.interval_for_visit == 0:
            raise UserError(_('Interval for visit must be big then 0'))

        recs = []

        d_day = self.start_week_day.day
        d_month = self.start_week_day.month
        d_year = self.start_week_day.year

        while d_day < self.finish_week_day.day:
            t_delta_start = timedelta(hours=self.time_start_job)
            t_delta_finish = timedelta(hours=self.time_finish_job)
            t_min = datetime(d_year, d_month, d_day) + t_delta_start
            t_max = datetime(d_year, d_month, d_day) + t_delta_finish

            while t_min < t_max:
                obj = {'doctor_id': self.doctor_id.id,
                       'visit_date': t_min,
                       'visit_start_datetime': t_min}
                recs.append(obj)
                t_min += timedelta(minutes=self.interval_for_visit)
            d_day += 1

        self.env['hr_hospital.schedule_of_doctor'].create(recs)

    @staticmethod
    def action_open_wizard():
        return {
            'name': _('Create doctor schedule wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'create_doctor_schedule_wizard',
            'target': 'new',
        }
