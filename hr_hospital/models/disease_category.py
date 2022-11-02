import logging
from odoo.exceptions import ValidationError

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class DiseaseCategory(models.Model):
    _name = 'hr_hospital.disease_category'
    _description = 'Disease category'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string='Name',
                       index=True,
                       required=True)
    complete_name = fields.Char(comodel_name='Complete Name',
                                compute='_compute_complete_name',
                                recursive=True,
                                store=True)
    parent_id = fields.Many2one(comodel_name='hr_hospital.disease_category',
                                string='Disease Category',
                                index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(comodel_name='hr_hospital.disease_category',
                                inverse_name='parent_id',
                                string='Child Categories')
    disease_count = fields.Integer(string='# Disease',
                                   compute='_compute_disease_count',
                                   help="The number of disease under this category")
    active = fields.Boolean(default=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        for obj in self:
            obj.disease_count = self.env['hr_hospital.disease'].search_count([('category_id', 'child_of', obj.id)])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
