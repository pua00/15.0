import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class VisitDoctor(models.Model):
    _name = 'hr_hospital.visit_doctor'
    _description = 'Visit doctor'

    def _get_research_domain(self):
        for rec in self:
            print(rec.patient_id)
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
    diagnosis_id = fields.Many2one(comodel_name='hr_hospital.diagnosis',
                                   string='Diagnose of patient',
                                   index=True)
    recommendation = fields.Text(string='Recommendation')
    active = fields.Boolean(default=True)
    research_ids = fields.Many2many('hr_hospital.research',
                                    string='Researches')
    state = fields.Selection(string='Visit status',
                             selection=[('plan', "Plan"),
                                        ('done', "Done"),
                                        ('cancel', "Cancel")],
                             default='plan', required=True)

    def action_set_status_plan(self):
        for rec in self:
            rec.state = 'plan'

    def action_set_status_done(self):
        for rec in self:
            rec.state = 'done'

    def action_set_status_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.ondelete(at_uninstall=False)
    def _unlink_only_if_empty(self):
        if len(self.research_ids) > 0:
            raise UserError(_('Visit has research. Delete not possible'))
        if self.diagnosis_id:
            raise UserError(_('Visit has diagnosis. Delete not possible'))

    def name_get(self):
        return [(tag.id, 'Visit {}: {} = > {}'.format(self.visit_time or "",
                                                      tag.doctor_id.name or "",
                                                      tag.patient_id.name or "")) for tag in self]
