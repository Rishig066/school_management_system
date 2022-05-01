# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class SchoolManagementTeacher(models.Model):
    _name = "school.teacher"  # ----------------model name--------------
    _description = "student details"

    # fields ------------------------------------------------------------
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    contact = fields.Char(string='Contact No', required=True)
    student_id = fields.One2many("school.student", 'name', string="Students")
    specialists = fields.Char(string='Specialists', required=True)
    address = fields.Char(string='Address', required=True)
    total = fields.Integer(compute='_compute_total')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')

    note = fields.Text(string='Description')


    def _compute_total(self):
        self.total = self.env['school.student'].search_count([('cc_name', '=', self.id)])