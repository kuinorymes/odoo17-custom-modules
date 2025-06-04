from odoo import models, fields, api


class CrmLeadProductLine(models.Model):
    _name = "crm.lead.product.line"
    _description = "CRM Lead Product Line"

    description = fields.Text(string="Description")
    product_quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Price per unit")
    price_subtotal = fields.Float(
        string="Subtotal price",
        compute="_compute_price_subtotal",
        store=True
    )
    lead_id = fields.Many2one(
        "crm.lead",
        string="Lead",
        required=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True
    )

    @api.depends("product_quantity", "price_unit")
    def _compute_price_subtotal(self):
        for record in self:
            record.price_subtotal = record.product_quantity * record.price_unit


class CrmLead(models.Model):
    _inherit = "crm.lead"

    product_line_ids = fields.One2many(
        "crm.lead.product.line",
        "lead_id",
        string="Products",
    )
