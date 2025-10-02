{
    'name': 'CRM Lead products',
    'version': '1.0',
    'summary': 'Extend CRM Lead module with product adding',
    'category': 'CRM',
    'license': 'OPL-1',
    "price": 10.0,
    "currency": "EUR",
    'depends': ['crm', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_product_views.xml',
        'views/crm_lead_product_package.xml',
        'wizard/crm_lead_add_package_wizard_views.xml'
    ],
    'images': [
        'static/description/banner.gif',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
