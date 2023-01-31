# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentInfo(models.Model):
    _name = "attendance.student"
    _description = "All informations about is here."
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char("Name", required=True)
    is_readonly = fields.Boolean('Readonly',default=False,compute ="_is_readonly")
    student_id = fields.Char("Student Id", required=True)
    email = fields.Char("Email")
    course_id = fields.Many2one("attendance.course", string="Student Course")
    year = fields.Integer("Year")
    semester = fields.Integer("Semester")
    date = fields.Date("Date", default=fields.Datetime.now())
    subject_id = fields.Many2one(
        "attendance.subject", string="Subject", tracking=True)
    faculty_id = fields.Many2one("attendance.faculty", string="Faculty",
                                 tracking=True, domain="[('subject_id','=',subject_id)]")
    department_name_id = fields.Many2one(
        "attendance.department", string="Department")
    state = fields.Selection(selection=[('pending', 'Pending'), (
        'done', 'Done'), ('absent', 'Absent')], default="pending", tracking=True)
    active = fields.Boolean(default=True)
    student_progress_ids = fields.Many2many(
        'attendance.progress', string="Student Progress")
    image = fields.Binary()

    @api.constrains('semester', 'year')
    def _check_year_semester(self):
        for rec in self:
            temp = rec.year
            if (temp*2) != rec.semester and (temp*2)-1 != rec.semester:
                raise ValidationError('Enter Valid Year Or Semester')

    def done_action(self):
        for rec in self:
            rec.state = 'done'

    def absent_action(self):
        for rec in self:
            rec.state = 'absent'

    @api.ondelete(at_uninstall=False)
    def _delete_permission(self):
        for rec in self:
            if rec.state == "done":
                raise ValidationError("You can't Remove Done Attendance")

    def render_form_view(self,model_name,query):
        form_view_id = self.env[model_name].search([('name','=',query)]).id
        print("-------------",form_view_id,model_name,query)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Progress',
            'view_mode': 'form',
            'res_model': model_name,
            'res_id' : form_view_id,
            'target': 'current'
            }
    def attendance_subject_button(self):
        return self.render_form_view('attendance.subject',self.subject_id.name)

    def attendance_faculty_button(self):
        return self.render_form_view('attendance.faculty',self.faculty_id.name)

    def attendance_department_button(self):
        return self.render_form_view('attendance.department',self.department_name_id.name)

    def _is_readonly(self):
        for rec in self:
            usr = self.env['res.users'].browse(self.env.uid)
            if usr.has_group('attendance.attendance_group_user'):
                rec.is_readonly = True
            else:
                rec.is_readonly = False
