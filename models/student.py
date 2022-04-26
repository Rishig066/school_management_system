# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SchoolManagement(models.Model):
    _name = "school.student"        # ----------------model name--------------
    _description = "student details"

    # fields ------------------------------------------------------------
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    roll_no = fields.Char(string='Roll No', required=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')

    note = fields.Text(string='Description')
