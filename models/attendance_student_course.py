# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentCourseInfo(models.Model):
    _name = "attendance.course"
    _description = "All informations about course is here."

    name = fields.Char(required = True)