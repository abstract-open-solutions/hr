# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2015 Giacomo Spettoli (giacomo.spettoli@abstract.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Leave Management - UOM',
    'description': """""",
    'version': '1.0',
    'author': 'Abstract srl',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': 'Holidays UOM',
    'website': 'https://www.abstract.it',
    'depends': [
        'product',
        'hr_holidays',
        'hr_contract'
    ],
    'data': [
        'views/hr_holidays_view.xml'
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
