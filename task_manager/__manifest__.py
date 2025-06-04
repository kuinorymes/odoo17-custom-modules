{
    'name': 'Task Manager',
    'version': '1.0',
    'summary': 'Manage project tasks with contacts, chatter and attachments',
    'depends': ['base', 'mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/task_images_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}