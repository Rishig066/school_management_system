# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SchoolManagement(models.Model):
    _name = "school.teacher"  # ----------------model name--------------
    _description = "student details"

    # fields ------------------------------------------------------------
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    contact = fields.Char(string='Contact No', required=True)
    student_id = fields.One2many("school.student", 'name', string="Students")
    specialists = fields.Char(string='Specialists', required=True)
    address = fields.Char(string='Address', required=True)


    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')

    note = fields.Text(string='Description')
