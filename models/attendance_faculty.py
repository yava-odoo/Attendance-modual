# -*- coding: utf-8 -*-

from odoo import models, fields

class FaclutyInfo(models.Model):
    _name = "attendance.faculty"
    _description = "All informations about subject faculty and other members of the collage."
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(required = True)
    email = fields.Char("Email")
    subject = fields.Many2many('attendance.subject',string="Subject",tracking=True)
    department_name = fields.Many2one("attendance.department" ,string="Department",tracking=True)
    active = fields.Boolean(default=True)
    course = fields.Many2many("attendance.course", string="Course")