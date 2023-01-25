# -*- coding: utf-8 -*-

{
    'name': "Attendance Odoo",
    'version': '1.0',
    'author': "yava",
    'description': "attendance is here",
    'depends':['hr_attendance','attendance'],
    'data':[
        'views/attendance_faculty.xml'
    ],
    'application': True,
    'installable': True,
    'license' : "LGPL-3",
    'website': 'https://www.odoo.com',
}