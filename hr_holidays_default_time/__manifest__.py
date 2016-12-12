# -*- coding: utf-8 -*-
# Copyright 2016 Davide Corio
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Holidays Default Time',
    'summary': """
        Leaves default time""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Davide Corio,Odoo Community Association (OCA)',
    'website': 'http://www.abstract.it',
    'depends': [
        'web_calendar',
        'hr_holidays'
    ],
    'data': [
        'views/hr_holidays_view.xml',
    ],
    'demo': [
    ],
}
