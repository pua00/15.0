import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ChangeVisitToDoctorWizard(models.TransientModel):
    _name = 'change_visit_to_doctor_wizard'
    _description = _('Change visit to doctor wizard')

    old_doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                    string='Old Doctor',
                                    readonly=True,
                                    required=True)
    visit_doctor_id = fields.Many2one(comodel_name='hr_hospital.visit_doctor',
                                      string='Visit doctor',
                                      readonly=True,
                                      required=True)
    old_visit_date = fields.Date(string='Old Visit date',
                                 required=True,
                                 readonly=True,
                                 index=True)
    old_schedule_of_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.schedule_of_doctor',
        string='Old Schedule of Doctor',
        readonly=True,
        required=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='New Doctor',
                                required=True)
    visit_date = fields.Date(string='New Visit date',
                             required=True,
                             index=True)
    schedule_of_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.schedule_of_doctor',
        string='New Schedule of Doctor',
        required=True)

    def action_start_wizard(self):
        record = self.env.context["active_id"]
        visit = self.env['hr_hospital.visit_doctor']
        info_for_change = {
            'doctor_id': self.doctor_id,
            'schedule_of_doctor_id': self.schedule_of_doctor_id,
            'visit_time': self.schedule_of_doctor_id.visit_start_datetime}
        if record:
            el_visit = visit.browse(record)
            el_visit.write(info_for_change)

    @api.onchange('visit_date')
    def _on_change_visit_day(self):
        self.doctor_id = False
        self.schedule_of_doctor_id = False
