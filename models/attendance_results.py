# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentResult(models.Model):
    _name = "attendance.result"
    _description = "All informations about student's past academic results"

    name = fields.Char('Exam',required = True)
    seat_no = fields.Char(string="Seat No.")
    cgpa = fields.Float('CGPA/% Obtained')
    percentile = fields.Float('Percentile')
    year = fields.Integer('Year')
    month = fields.Char('Month')
    bord = fields.Char('Bord/University')
    groups = fields.Char('Group/Specialisation')
    student_results_id = fields.Many2one('attendance.student',string="Student Results")
