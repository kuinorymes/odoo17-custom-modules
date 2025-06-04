{
    'name': 'Task Manager Weight Extension',
    'version': '1.0',
    'summary': 'Extend Task Manager module with weight calculations',
    'depends': ['base', 'mail', 'contacts', 'task_manager'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_weight_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}