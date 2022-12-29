# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentCourseInfo(models.Model):
    _name = "attendance.course"
    _description = "All informations about course is here."

    name = fields.Char(required = True)
    active = fields.Boolean(default=True)
    # department_id = fields.Many2one('attendance.department' ,string="Department Id")