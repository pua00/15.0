import logging

from odoo import fields, models

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
    active = fields.Boolean(default=True)
