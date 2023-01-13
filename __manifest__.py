# -*- coding: utf-8 -*-

{
    'name': "Attendance",
    'version': '1.0',
    'author': "yava",
    'description': "Attendace is now easy by using this modual",
    'depends':['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/attendance_student_data.xml',
        'views/attendance_menuitems.xml',
        'views/attendance_student_views.xml',
        'views/attendance_faculty_views.xml',
        'views/attendance_department_views.xml',
        'views/attendance_student_course.xml',
        'views/attendance_subject_views.xml',
        'views/attedance_progress_views.xml',
    ],
    'demo' : [
        'demo/attendance_progress_demo_data.xml',
        'demo/attendance_department_demo_data.xml',
        'demo/attendance_course_demo_data.xml',
        'demo/attendance_subject_demo_data.xml',                                                                                                
        'demo/attendance_faculty_demo_data.xml',
        'demo/attendance_student_demo_data.xml',
    ],
    'application': True,
    'installable': True,
    'license' : "LGPL-3",
    'website': 'https://www.odoo.com',


}