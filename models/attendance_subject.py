# -*- coding: utf-8 -*-

from odoo import models, fields

class SubjectInfo(models.Model):
    _name = "attendance.subject"
    _description = "All information about the subjects in Collage"

    name = fields.Char(required = True)
    semester = fields.Integer("Semester")
    faculty = fields.Many2one("attendance.faculty" ,string="Faculty")
    department_name = fields.Many2many("attendance.department" ,string="Department")
    course = fields.Many2many("attendance.course", string="Student Course")