{
    'name': 'Website Monitor',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Monitor website URL and port, email alerts, manual check, status in header',
    'author': 'Your Name',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/monitor_views.xml',
        'data/monitor_cron.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
