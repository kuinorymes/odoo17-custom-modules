{
    'name': 'Helpdesk Ticket Extension',
    'version': '1.0',
    'summary': 'Extend Helpdesk with adding Project Task to ticket',
    'category': 'Helpdesk',
    'depends': ['helpdesk', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_create_task_wizard_views.xml',

        
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
