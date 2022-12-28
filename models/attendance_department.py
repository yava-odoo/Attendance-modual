# -*- coding: utf-8 -*-

from odoo import models, fields

class DepartmentInfo(models.Model):
    _name = "attendance.department"
    _description = "All informations about is here."

    name = fields.Char(required = True)
    # course = fields.Many2many("attendance.course", string="Student Course")