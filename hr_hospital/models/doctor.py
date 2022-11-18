import logging
from datetime import datetime
from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'
    _inherit = {'hr_hospital.person': 'person_id'}

    person_id = fields.Many2one(comodel_name='hr_hospital.person',
                                string='Person')
    profession = fields.Char(required=True)
    is_intern = fields.Boolean(string='This is doctor-intern')
    doctor_mentor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                       string='Doctor (as mentor)',
                                       domain=[('is_intern', "=", False)])
    intern_ids = fields.One2many(
        string='List of interns',
        comodel_name='hr_hospital.doctor',
        inverse_name='doctor_mentor_id'
    )
    patient_ids = fields.One2many(
        string='List of patients',
        comodel_name='hr_hospital.patient',
        inverse_name='personal_doctor_id'
    )
    visit_ids = fields.One2many(
        string='List of visits',
        comodel_name='hr_hospital.visit_doctor',
        inverse_name='doctor_id'
    )

    active = fields.Boolean(default=True)

    def action_make_new_visit_to_doctor(self):
        # for rec in self:
        ctx = {
            'default_visit_time':
                datetime.now(),
            'default_doctor_id':
                self.id,

        }

        return {
            'name': _('Visit doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr_hospital.visit_doctor',
            'target': 'new',
            'context': ctx,
        }

    def get_doctor_profession(self):
        self.ensure_one()
        return f'{self.profession}'
