# -*- coding: utf-8 -*-
from itertools import count

from odoo import api, fields, models, _, tools


class SchoolManagementStudent(models.Model):
    _inherit = "sale.order"  # ----------------model name--------------

    # fields ------------------------------------------------------------
    new_fi = fields.Char(string='New field')






