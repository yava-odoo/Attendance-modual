# -*- coding: utf-8 -*-

from odoo import models, fields

class SubjectInfo(models.Model):
    _name = "attendance.subject"
    _description = "All information about the subjects in Collage"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(required = True)
    semester = fields.Integer("Semester")
    faculty_ids = fields.One2many("attendance.faculty" ,'subject_id',string="Faculty",tracking=True)
    department_name_ids = fields.Many2many("attendance.department" ,string="Department",tracking=True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string='Color Index')
    student_ids = fields.One2many('attendance.student','subject_id',string='Student')
    student_count = fields.Integer(compute = "_student_count" ,string="Student Count")      


    def get_student(self):
        return {
           'type': 'ir.actions.act_window',
            'name': 'Students',
            'view_mode': 'tree,form',
            'res_model': 'attendance.student',
            'domain': [('subject_id', '=', self.id)],
        }

    def _student_count(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)