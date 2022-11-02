import logging

from odoo import api, exceptions, fields, models, _

_logger = logging.getLogger(__name__)


class ScheduleOfDoctor(models.Model):
    _name = 'hr_hospital.schedule_of_doctor'
    _description = 'Schedule of Doctor'

    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True, index=True)
    visit_date = fields.Date(string='Date',
                             required=True)
    visit_start_datetime = fields.Datetime(string='Visit start from',
                                           required=True)
    active = fields.Boolean(default=True)

    def name_get(self):
        return [(tag.id, '{}: {}'.format(tag.doctor_id.name or "",
                                         tag.visit_start_datetime or "")) for tag in self]

    @api.constrains('doctor_id, visit_start_datetime')
    def _check_existing_record(self):
        records = self.search([('visit_start_datetime', '=', self.visit_start_datetime),
                               ('doctor_id', '=', self.doctor_id.id)])
        _logger.debug('sizes---', len(records))
        if len(records) > 0:
            raise exceptions.ValidationError(_('{} This date for {} is busy'.format(self.visit_start_datetime,
                                                                                    self.doctor_id.name)))
