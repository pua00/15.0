{
    'name': "hr_hospital",

    'summary': """Short description of module's purpose""",

    'author': "Ruslan Panchenko",
    'website': "http://mysite.com",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': [],
    'external_dependencies': {'python': [], },

    'data': [

        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/diagnosis.xml',
        'views/patient_card.xml',

    ],
    'demo': [],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 0,
    'currency': 'EUR',

}
