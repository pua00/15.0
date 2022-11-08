import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class ChangeDoctorMultyWizard(models.TransientModel):
    _name = 'change_doctor_multy_wizard'
    _description = _('Wizard for easy way to change doctor')

    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Doctor',
                                required=True)

    def action_start_wizard(self):
        records = self.env.context["active_ids"]
        patients = self.env['hr_hospital.patient']
        info_for_change = {'personal_doctor_id': self.doctor_id}
        if records:
            for rec in records:
                el_patient = patients.browse(rec)
                el_patient.write(info_for_change)

    @staticmethod
    def action_open_wizard():
        return {
            'name': _('Wizard for easy way to change doctor'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'change_doctor_multy_wizard',
            'target': 'new',
        }
