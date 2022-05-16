# -*- coding: utf-8 -*-
from itertools import count

from odoo import api, fields, models, _, tools


class SchoolManagementStudent(models.Model):
    _name = "school.student"  # ----------------model name--------------
    _description = "student details"

    # fields ------------------------------------------------------------
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    cc_name = fields.Many2one('school.teacher')
    roll_no = fields.Char(string='Roll No', required=True)

    standard = fields.Selection([('tenth', '10th'), ('eleven', '11th'), ('twelve', '12th')], required=True, default='10th')

    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True, default='male')

    note = fields.Text(string='Description')
