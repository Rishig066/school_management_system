# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School management',
    'version': '1.0',
    'summary': '',
    'sequence': 10,
    'description': """school management software""",
    'category': '',
    'website': '',
    'images': [],
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/email.xml',
        'views/menu_or_action.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/sale.xml',
        'views/class_room.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
