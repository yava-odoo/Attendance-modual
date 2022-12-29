# -*- coding: utf-8 -*-

from odoo import models, fields

class DepartmentInfo(models.Model):
    _name = "attendance.department"
    _description = "All informations about is here."

    name = fields.Char(required = True)
    active = fields.Boolean(default=True)
    # subject_ids = fields.One2many('attendance.subject','department_name',string="Subjects")
    # course_ids = fields.One2many("attendance.course", 'department_id',string="Student Course")