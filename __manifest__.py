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
        'views/student.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
