from odoo import models, fields


class HelpdeskCreateTaskWizard(models.TransientModel):
    _name = "helpdesk.create.task.wizard"
    _description = "Create Task for ticket"

    helpdesk_ticket_id = fields.Many2one(
        "helpdesk.ticket",
        string="Helpdesk Ticket",
        readonly=True,
    )
    name = fields.Char(string="Task Name", required=True)
    project_id = fields.Many2one(
        "project.project",
        string="Project",
        required=True
    )
    user_ids = fields.Many2many("res.users", string="Users")
    partner_id = fields.Many2one("res.partner", string="Customerso")
    tag_ids = fields.Many2many("project.tags", string="Tags")
    company_id = fields.Many2one("res.company", string="Company", readonly=True)
    description = fields.Text(string="Task Description")

    def create_task(self):
        self.ensure_one()

        task_vals = {
            "name": self.name,
            "project_id": self.project_id.id,
            "user_ids": [(6, 0, self.user_ids.ids)],
            "partner_id": self.partner_id.id,
            "tag_ids": [(6, 0, self.tag_ids.ids)],
            "company_id": self.company_id.id,
            "description": self.description,
        }

        task = self.env["project.task"].create(task_vals)

        return {
            "type": "ir.actions.act_window",
            "res_model": "project.task",
            "view_mode": "form",
            "res_id": task.id,
            "target": "current",
            "context": {"create": False},
        }