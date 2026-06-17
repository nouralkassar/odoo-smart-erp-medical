{
    'name': 'Smart Hospital Pulse',
    'version': '1.0',
    'summary': 'Simulated IoT vitals monitoring and automated triage alerts',
    'description': 'Adds heart-rate monitoring fields, API endpoint, and automatic critical triage logic.',
    'category': 'Healthcare',
    'author': 'Smart Hospital Team',
    'depends': ['crm'],
    'data': [
        'views/crm_triage_views.xml',
    ],
    'installable': True,
    'application': True,
}
