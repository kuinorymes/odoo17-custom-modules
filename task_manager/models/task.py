from odoo import models, fields


class TaskModel(models.Model):
    _name = "task"
    _description = "Project task"
    _order = "priority desc"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Task Name", required=True)
    description = fields.Text(string="Task Description", required=True)
    deadline = fields.Date(string="Deadline")
    created_at = fields.Datetime(string="Created at", default=fields.Datetime.now, readonly=True)
    difficulty = fields.Integer(string="Difficulty", default=5)
    is_active = fields.Boolean(string="Active", default=True)

    priority = fields.Selection([
        ("0", "Low"),
        ("1", "Normal"),
        ("2", "High"),
    ], string="Task Priority", required=True)

    status = fields.Selection([
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled")
    ], string="Task Status", tracking=True)


    partner_id = fields.Many2one("res.partner", string="Client")
    image_ids = fields.One2many("task.image", "task_id", string="Images")
    assigned_to = fields.Many2many("res.users", string="Assigned to")