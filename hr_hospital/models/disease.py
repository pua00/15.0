import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Disease', required=True)
    category_id = fields.Many2one('hr_hospital.disease_category', 'Disease Category', index=True, ondelete='cascade', required=True)
    active = fields.Boolean(default=True)

