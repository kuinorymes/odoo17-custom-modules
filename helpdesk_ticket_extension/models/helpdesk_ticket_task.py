from odoo import models, fields, api
from odoo.exceptions import AccessError
from odoo.tools import html2plaintext


class HelpdeskTicketTask(models.Model):
    _inherit = "helpdesk.ticket"

    user_has_task_access = fields.Boolean(
        compute="_compute_user_has_task_access",
        string="Can Create Task"
    )

    @api.depends("user_id")
    def _compute_user_has_task_access(self):
        for record in self:
            current_user = self.env.user
            is_assigned_user = record.user_id.id == current_user.id
            is_helpdesk_admin = current_user.has_group("helpdesk.group_helpdesk_manager")

            record.user_has_task_access = is_assigned_user or is_helpdesk_admin

    def create_task_wizard(self):
        self.ensure_one()

        if not self.user_has_task_access:
            raise AccessError("You are not allowed to create tasks")

        return {
            "name": "Create Task",
            "type": "ir.actions.act_window",
            "res_model": "helpdesk.create.task.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {
                "default_helpdesk_ticket_id": self.id,
                "default_name": self.name,
                "default_description": html2plaintext(self.description),
                "default_company_id": self.company_id.id,
                "default_partner_id": self.partner_id.id,
            },
        }