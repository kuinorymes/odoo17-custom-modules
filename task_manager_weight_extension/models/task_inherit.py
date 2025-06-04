from odoo import models, fields, api

class TaskInherit(models.Model):
    _inherit = "task"

    weight_kg = fields.Float(string="Weight (kg)", tracking=True)
    weight_ton = fields.Float(
        string="Weight (ton)",
        compute="_compute_weight_ton",
        inverse="_inverse_weight_ton",
        store=True,
        tracking=True,
    )

    @api.depends("weight_kg")
    def _compute_weight_ton(self):
        for record in self:
            record.weight_ton = record.weight_kg / 1000

    def _inverse_weight_ton(self):
        for record in self:
            record.weight_kg = record.weight_ton * 1000