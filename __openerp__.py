# -*- coding: utf-8 -*-

{
    'name': "Events Attachments",
    'category': 'Hidden',
    'summary': "Publish Your Event's Attachments",
    'website': 'https://www.odoo.com/page/events',
    'version': '1.0',
    'description': """
Online Event's Tickets
======================

        """,
    'author': 'Moldeo Interactive',
    'depends': ['website_event', 'document'],
    'data': [
        'views/website_event_attachments.xml',
        'security/website_event_attachments_config.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False
}
