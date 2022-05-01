# -*- coding: utf-8 -*-
from itertools import count

from odoo import api, fields, models, _, tools


class SchoolManagementStudent(models.Model):
    _name = "school.class_room"  # ----------------model name--------------
    _description = "class room details"

    # fields ------------------------------------------------------------

    cc_name = fields.Char(string='CC Name', required=True)

    students_id = fields.Integer(compute='_compute_total')
    no_of_tables = fields.Integer(string='No Of Tables')
    no_of_fan = fields.Integer(string='No of Fan', default=2)
    note = fields.Text(string='Description')
