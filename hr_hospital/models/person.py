import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Person(models.Model):
    _name = 'hr_hospital.person'
    _description = 'Abstract person'

    name = fields.Char(string='Full name', required=True)
    gender = fields.Selection(string='Gender', selection=[('male', "Male"), ('femail', "Femail")], default='male',
                              required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='E-Mail')
    photo = fields.Image(string='Photo of person', max_width=512, max_height=512)
