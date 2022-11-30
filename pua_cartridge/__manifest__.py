{
    'name': "Repair Cartridge",

    'summary': """Refilling cartridges for printers""",

    'author': "Ruslan Panchenko",
    'website': "http://mysite.com",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base', 'product'],
    'external_dependencies': {'python': [], },

    'data': [
        'security/pua_cartridge_groups.xml',
        'security/ir.model.access.csv',

        'wizard/change_repair_cartridge_multy_wizard_views.xml',

        'report/model_repair_cartridge.xml',
        'report/model_repair_cartridge_templates.xml',

        'views/pua_cartridge_menus.xml',
        'views/shelf_views.xml',
        'views/engineer_views.xml',
        'views/type_of_cartridge_views.xml',
        'views/cartridge_views.xml',
        'views/partner_views.xml',
        'views/product_views.xml',
        'views/repair_cartridge_views.xml',

    ],
    'demo': [
        'data/pua_cartridge_engineer_demo.xml',
        'data/pua_cartridge_shelf_demo.xml',
        'data/pua_cartridge_type_of_cartridge_demo.xml',
        'data/pua_cartridge_cartridge_demo.xml',
        'data/pua_cartridge_product_demo.xml',
        'data/pua_cartridge_repair_cartridge_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [

    ],

    'price': 100,
    'currency': 'EUR',

}
