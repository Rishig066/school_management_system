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
    'depends': [],
    'data': [
        'views/menu_or_action.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/class_room.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
