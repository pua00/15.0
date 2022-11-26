{
    'name': "pua_cartridge",

    'summary': """Refilling cartridges for printers""",

    'author': "Ruslan Panchenko",
    'website': "http://mysite.com",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],
    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',

        'views/pua_cartridge_menus.xml',
        'views/shelf_views.xml',
        'views/engineer_views.xml',

    ],
    'demo': [
        'data/pua_cartridge_engineer_demo.xml',
        'data/pua_cartridge_shelf_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 100,
    'currency': 'EUR',

}
