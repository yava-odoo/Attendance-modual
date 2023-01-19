# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentResult(models.Model):
    _inherit = 'attendance.student'
    
    school_name = fields.Char('School/Collage Name')
    states = fields.Char('State')
    city = fields.Char('City')
    country_id = fields.Many2one('res.country',string="Country")
    results_ids = fields.One2many('attendance.result','student_results_id',string="Results")