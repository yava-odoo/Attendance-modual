# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentInfo(models.Model):
    _name = "attendance.student"
    _description = "All informations about is here."
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char("Name", required=True)
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

    @api.depends('state')
    def done_action(self):
        for rec in self:
            rec.state = 'done'

    @api.ondelete(at_uninstall=False)
    def _delete_permission(self):
        for rec in self:
            if rec.state == "done":
                raise ValidationError("You can't Remove Done Attendance")

    # def new_action(self):

    #     for rec in self:
    #         self.env['attendance.progress'].create({
    #             'name' : rec.name
    #         })
    #     return{
    #         'type': 'ir.actions.act_window',
    #         'name': 'Progress',
    #         'view_mode': 'form',
    #         'res_model': 'attendance.progress',
    #         'domain' : [('name','=',self.name)]
    #     }