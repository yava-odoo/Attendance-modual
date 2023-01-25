# -*- coding: utf-8 -*-

from odoo import models, fields

class FaclutyInfo(models.Model):
    _name = "attendance.progress"
    _description = "All informations about student's Progress."

    name = fields.Char(required = True)
    color = fields.Integer(string="Color")
