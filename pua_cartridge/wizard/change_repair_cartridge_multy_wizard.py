import logging

from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class ChangeRepairCartridgeMultyWizard(models.TransientModel):
    _name = 'change_repair_cartridge_multy_wizard'
    _description = _('Wizard for easy way to change state repair cartridge')

    state = fields.Selection(string='Work status',
                             selection=[('enter', "Enter"),
                                        ('done', "Done"),
                                        ('return', "Return")],
                             default='return', required=True)

    def action_start_wizard(self):
        records = self.env.context["active_ids"]
        docs = self.env['pua_cartridge.repair_cartridge']
        info_for_change = {'state': self.state}
        if records:
            for rec in records:
                el_doc = docs.browse(rec)
                el_doc.write(info_for_change)

    @staticmethod
    def action_open_wizard():
        return {
            'name': _('Wizard for easy way to change state repair cartridge'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'change_repair_cartridge_multy_wizard',
            'target': 'new',
        }
