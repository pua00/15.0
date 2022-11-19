import datetime
import logging

from odoo import api, exceptions, fields, models, _

# from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class VisitDoctor(models.Model):
    _name = 'hr_hospital.visit_doctor'
    _description = 'Visit doctor'

    def _get_research_domain(self):
        for rec in self:
            return [('patient_id', 'in', rec.patient_id)]

    visit_time = fields.Datetime(string='Visit time',
                                 required=True,
                                 index=True)
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True,
                                index=True)
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient',
                                 string='Patient',
                                 required=True,
                                 index=True)
    recommendation = fields.Text()
    active = fields.Boolean(default=True)
    state = fields.Selection(string='Visit status',
                             selection=[('plan', "Plan"),
                                        ('done', "Done"),
                                        ('cancel', "Cancel")],
                             default='plan', required=True)
    severity = fields.Selection(string='Visit status',
                                selection=[('easy', "Easy"),
                                           ('average', "Average"),
                                           ('hard', "Hard")],
                                default='average', required=True)

    schedule_of_doctor_id = fields.Many2one(
        comodel_name='hr_hospital.schedule_of_doctor',
        string='Schedule of Doctor')
    duration = fields.Float()

    def action_set_status_plan(self):
        for rec in self:
            rec.state = 'plan'

    def action_set_status_done(self):
        for rec in self:
            rec.state = 'done'

    def action_set_status_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def write(self, vals):
        visit_doctor = super(VisitDoctor, self).write(vals)
        check_date = datetime.datetime.now() - datetime.timedelta(days=30)
        if self.env.user.has_group(
                'hr_hospital.group_hr_hospital_user') \
                and self.visit_time < check_date:
            raise exceptions.UserError(
                _('May change document only last 30 days'))

        return visit_doctor

    @api.ondelete(at_uninstall=False)
    def _unlink_only_if_empty(self):
        pass
        # Зробити перевірку
        # if len(self.research_ids) > 0:
        #     raise UserError(_('Visit has research. Delete not possible'))
        # if self.diagnosis_id:
        #     raise UserError(_('Visit has diagnosis. Delete not possible'))

    # def name_get(self):
    #  Видає помилку при виборі в інших об'єктах
    #     print('name_get')
    #     return [(tag.id, 'Visit {}: {} = > {}'
    #              .format(self.visit_time or "",
    #                      tag.doctor_id.name or "",
    #                      tag.patient_id.name or "")) for tag in self]

    def action_open_change_visit_to_doctor_wizard(self):
        if len(self.env.context['active_ids']) != 1:
            raise exceptions.UserError(_('May select only ONE visit'))

        current_visit = self.env['hr_hospital.visit_doctor'].browse(
            self.env.context['active_id'])
        if current_visit.state != 'plan':
            raise exceptions.UserError(_('May select visit in state ONLY plan'))

        return {
            'name': _('Wizard for easy way to Change visit to doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'change_visit_to_doctor_wizard',
            'target': 'new',
            'context': {
                'default_old_doctor_id':
                    current_visit.doctor_id.id,
                'default_old_visit_date':
                    current_visit.schedule_of_doctor_id.visit_date,
                'default_visit_date':
                    current_visit.schedule_of_doctor_id.visit_date,
                'default_visit_doctor_id':
                    current_visit.id,
                'default_old_schedule_of_doctor_id':
                    current_visit.schedule_of_doctor_id.id,
            }
        }
