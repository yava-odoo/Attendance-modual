# -*- coding: utf-8 -*-

from odoo import models, fields

class DepartmentInfo(models.Model):
    _name = "attendance.department"
    _description = "All informations about is here."

    name = fields.Char(required = True)
    active = fields.Boolean(default=True)
    color = fields.Integer(string='Color Index')
    student_ids = fields.One2many('attendance.student','department_name',string="Students")
    student_count = fields.Integer(compute = 'get_student',string="Student Count")


    def get_student(self):
        for rec in self:
            rec.student_count = len(rec.student_ids)

    def get_department_student(self):
        return {
           'type': 'ir.actions.act_window',
            'name': 'Students',
            'view_mode': 'tree,form',
            'res_model': 'attendance.student',
            'domain': [('department_name', '=', self.id)],
        }

