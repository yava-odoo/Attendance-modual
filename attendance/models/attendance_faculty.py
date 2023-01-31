# -*- coding: utf-8 -*-

from odoo import models, fields,api
from datetime import datetime

class FaclutyInfo(models.Model):
    _name = "attendance.faculty"
    _description = "All informations about subject faculty and other members of the collage."
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(required = True)
    email = fields.Char("Email")    
    subject_id = fields.Many2one('attendance.subject',string="Subject",tracking=True)
    department_name_id = fields.Many2one("attendance.department" ,string="Department",tracking=True)
    active = fields.Boolean(default=True)
    course_ids = fields.Many2many("attendance.course", string="Course")
    student_ids = fields.One2many('attendance.student','faculty_id',string="Students")
    image = fields.Binary()
    password = fields.Char("Password")

    @api.model
    def create(self,vals):
            id = self.env['res.users'].search([('name','=',vals['name'])]).id
            if not id:
                self.env['res.users'].create({
                    'name':vals['name'],
                    'login': vals['email'],
                    'password':vals['password'],
                })
            return super(FaclutyInfo,self).create(vals)