{
    'name': "hr_hospital",

    'summary': """Short description of module's purpose""",

    'author': "Ruslan Panchenko",
    'website': "http://mysite.com",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],  # Якщо модуль, не має прямих залежностей, він повінен мати залежність від базового модуля "base".
    'external_dependencies': {'python': [], },

    'data': [

        'security/ir.model.access.csv',

        'views/hr_hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/patient_card_views.xml',

    ],
    'demo': [],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 0,
    'currency': 'EUR',

}
