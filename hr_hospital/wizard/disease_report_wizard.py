import logging

from datetime import date
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class DiseaseReportWizard(models.TransientModel):
    _name = 'disease_report_wizard'
    _description = _('Disease report wizard')

    @api.model
    def year_selection(self):
        year = date.today().year
        start_year = year - 10
        year_list = []
        while year >= start_year:
            year_list.append((str(start_year), str(start_year)))
            start_year += 1
        return year_list

    @api.model
    def month_selection(self):
        month_list = []

        month_list.append(('1', 'January'))
        month_list.append(('2', 'February'))
        month_list.append(('3', 'March'))
        month_list.append(('4', 'April'))
        month_list.append(('5', 'May'))
        month_list.append(('6', 'June'))
        month_list.append(('7', 'July'))
        month_list.append(('8', 'August'))
        month_list.append(('9', 'September'))
        month_list.append(('10', 'October'))
        month_list.append(('11', 'November'))
        month_list.append(('12', 'December'))

        return month_list

    year = fields.Selection(selection=year_selection,
                            default='2022', required=True)
    month = fields.Selection(selection=month_selection,
                             default='1', required=True)

    @staticmethod
    def action_start_wizard():
        pass

    @staticmethod
    def action_open_wizard():
        return {
            'name': _('Disease report wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'disease_report_wizard',
            'target': 'new',
        }
