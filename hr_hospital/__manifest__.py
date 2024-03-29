{
    'name': "hr_hospital",

    'summary': """Short description of module's purpose""",

    'author': "Ruslan Panchenko",
    'website': "http://mysite.com",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],
    'external_dependencies': {'python': [], },

    'data': [

        'security/hr_hospital_groups.xml',
        'security/ir.model.access.csv',

        'data/hr_hospital_doctor_data.xml',

        'views/hr_hospital_menus.xml',
        'wizard/change_doctor_multy_wizard_views.xml',
        'wizard/create_doctor_schedule_wizard_views.xml',
        'wizard/change_visit_to_doctor_wizard_views.xml',
        'wizard/disease_report_wizard_views.xml',

        'report/model_doctor.xml',
        'report/model_doctor_templates.xml',

        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/disease_views.xml',
        'views/disease_category_views.xml',
        'views/contact_person_views.xml',
        'views/visit_doctor_views.xml',
        'views/personal_doctor_history_views.xml',
        'views/type_of_research_views.xml',
        'views/type_of_sample_views.xml',
        'views/research_views.xml',
        'views/schedule_of_doctor_views.xml',

    ],
    'demo': [
        'data/hr_hospital_doctor_demo.xml',
        'data/hr_hospital_doctor2_demo.xml'
    ],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 0,
    'currency': 'EUR',

}
