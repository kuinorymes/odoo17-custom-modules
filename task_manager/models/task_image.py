from odoo import models, fields


class TaskImageModel(models.Model):
    _name = "task.image"
    _description = "Task Image"

    task_id = fields.Many2one(
        "task",
        string="Task",
        ondelete="cascade"
    )
    image = fields.Image(string="Image")
    name = fields.Char(string="Image Description")
