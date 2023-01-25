from odoo import models, fields


class EstateAccount(models.Model):
    _inherit = 'attendance.faculty'

    start_time = fields.Datetime('Start')
    end_time = fields.Datetime('End')

    def time_start(self):
        for rec in self:
            rec.start_time = fields.Datetime().now()

    def time_end(self):
        for rec in self:
            rec.end_time = fields.Datetime().now()

    def submit_attendance(self):
        for rec in self:
            id = self.env['hr.employee'].search([('name','=',rec.name)]).id
            if not id:
                id = self.env['hr.employee'].create({
                    'name':rec.name
                }).id
            self.env['hr.attendance'].create({
                'check_in':rec.start_time,
                'check_out':rec.end_time,
                'employee_id':id,
            })
            return {
            'type': 'ir.actions.act_window',
            'name': 'faculty attendance',
            'view_mode': 'tree,form',
            'res_model': 'hr.attendance',
            }
        