# -*- coding: utf-8 -*-

from odoo import models, fields

class FaclutyInfo(models.Model):
    _name = "attendance.faculty"
    _description = "All informations about subject faculty and other members of the collage."

    name = fields.Char(required = True)
    email = fields.Char("Email")
    subject = fields.Many2many('attendance.subject',string="Subject")
    department_name = fields.Many2one("attendance.department" ,string="Department")
    active = fields.Boolean(default=True)
    course = fields.Many2many("attendance.course", string="Course")