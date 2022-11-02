import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class TypeOfResearch(models.Model):
    _name = 'hr_hospital.type_of_research'
    _description = 'Type of research'

    name = fields.Char(string='Type of research',
                       required=True)
    category_id = fields.Many2one(comodel_name='hr_hospital.type_of_research_category',
                                  string='Type of research Category',
                                  index=True,
                                  ondelete='cascade',
                                  required=True)
    active = fields.Boolean(default=True)
