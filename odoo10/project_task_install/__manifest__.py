# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'OS de Instalação',
    'version': '1.0',
    'category': 'Project Management',
    'depends': [
        'project',
        'hr_timesheet',
        'project_task_work',
        'br_sale',
        'seguranca'
    ],
    'data': [
        'data/task_sequence.xml',
        'views/project_view.xml',
        'views/sale_views.xml',
        'views/stock_picking_view.xml',
    ],
    'installable': True,
}