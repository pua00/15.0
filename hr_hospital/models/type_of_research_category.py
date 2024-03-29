import logging
from odoo.exceptions import ValidationError

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class TypeOfResearchCategory(models.Model):
    _name = 'hr_hospital.type_of_research_category'
    _description = 'Type of research category'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(index=True,
                       required=True)
    complete_name = fields.Char(
        compute='_compute_complete_name',
        recursive=True,
        store=True)
    parent_id = fields.Many2one(
        comodel_name='hr_hospital.type_of_research_category',
        string='Type of research Category',
        index=True,
        ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(
        comodel_name='hr_hospital.type_of_research_category',
        inverse_name='parent_id',
        string='Child Categories')
    type_of_research_count = fields.Integer(
        string='# Disease',
        compute='_compute_type_of_research_count',
        help="The number of type of research under this category")
    active = fields.Boolean(default=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_type_of_research_count(self):
        for obj in self:
            obj.type_of_research_count = self.env[
                'hr_hospital.type_of_research'].search_count(
                [('category_id', 'child_of', obj.id)])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
