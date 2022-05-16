# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class EmailWizard(models.TransientModel):
    _name = 'mail.update.wizard'
    _description = 'Create Automatic Entries'

    email = fields.Char(string='E-mail')
