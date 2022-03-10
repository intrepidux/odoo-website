##############################################################################
#
#    Odoo, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2019 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Toggle Record on Portal",
    "version": "14.0.1.0.0",
    "category": "",
    "summary": """""",
    "author": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://www.vertel.se/apps/website",
    "depends": [
        "sale",
        "account",
        "event",
        "project",
        "hr_timesheet",
        "skogsstyrelsen_translation",
        "website_event_portal_listing"
    ],
    "data": [
        "views/project_task_view.xml",
        "views/sale_order_view.xml",
        "views/account_view.xml",
        "views/timesheet_view.xml",
        "views/event_view.xml",
    ],
    "application": False,
    "installable": True,
}