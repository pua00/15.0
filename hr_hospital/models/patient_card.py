import logging

from odoo import fields, models  # модулі, що імпортуються повинні йти в алфавітному порядку

_logger = logging.getLogger(__name__)


class PatientCard(models.Model):  # У назві класів повинен використовуватися CamelCase. Назва повинна бути, як назва моделі (передавати своє значення).
    _name = 'hr_hospital.patient_card'
    _description = 'Patient card'

    name = fields.Char()
