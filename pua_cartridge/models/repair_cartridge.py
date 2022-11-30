import logging
from odoo import fields, models, _

_logger = logging.getLogger(__name__)


class RepairCartridge(models.Model):
    _name = 'pua_cartridge.repair_cartridge'
    _description = 'Repair cartridge'

    partner_id = fields.Many2one(comodel_name='res.partner',
                                 string='Partner',
                                 index=True,
                                 required=True)
    cartridge_id = fields.Many2one(
        comodel_name='pua_cartridge.cartridge',
        string='Cartridge',
        index=True,
        required=True)
    shelf_id = fields.Many2one(
        comodel_name='pua_cartridge.shelf',
        string='Shelf',
        index=True,
        required=True)
    doc_date = fields.Datetime(string='Document date',
                               default=fields.Date.today,
                               index=True,
                               required=True)
    repair_on_date = fields.Datetime(string='Repair on date',
                                     default=fields.Date.today,
                                     index=True,
                                     required=True)
    urgent_repair = fields.Boolean(string='Urgent repair')
    state = fields.Selection(string='Work status',
                             selection=[('enter', "Enter"),
                                        ('done', "Done"),
                                        ('return', "Return")],
                             default='enter', required=True)
    engineer_id = fields.Many2one(comodel_name='pua_cartridge.engineer',
                                  string='Engineer')
    active = fields.Boolean(default=True)

    def action_open_change_state_multy_wizard(self):
        # print(self, 'change_repair_cartridge_multy_wizard')
        return {
            'name': _('Wizard for easy way to change state repair cartridge'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'change_repair_cartridge_multy_wizard',
            'target': 'new',
        }

    def name_get(self):
        return [
            (tag.id, 'Doc repair {} = > {}'
             .format(self.doc_date or "",
                     tag.partner_id.name or ""))
            for tag in self]
