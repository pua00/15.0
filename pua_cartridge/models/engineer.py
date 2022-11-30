import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class Engineer(models.Model):
    _name = 'pua_cartridge.engineer'
    _description = 'Engineer'

    name = fields.Char(string='Engineer`s name',
                       required=True)
    gender = fields.Selection(selection=[('male', "Male"),
                                         ('female', "Female")],
                              default='male',
                              required=True)
    phone = fields.Char(string='Mobile phone')
    email = fields.Char(string='E-Mail')
    photo = fields.Image(string='Photo of person',
                         max_width=512,
                         max_height=512)
    active = fields.Boolean(default=True)
