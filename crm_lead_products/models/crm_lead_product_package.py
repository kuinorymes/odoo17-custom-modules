from odoo import models, fields


class CrmLeadProductPackage(models.Model):
    _name = "crm.lead.product.package"
    _description = "CRM Lead Product Package"

    name = fields.Char(string="Package Name", required=True)
    product_ids = fields.One2many(
        "crm.lead.product.package.line",
        "package_id",
        string="Package Products"
    )

class CrmLeadProductPackageLine(models.Model):
    _name = "crm.lead.product.package.line"
    _description = "CRM Lead Product Package Line"

    package_id = fields.Many2one(
        "crm.lead.product.package",
        string="Package",
        required=True,
        ondelete="cascade"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Product",
        required=True,
    )
    product_quantity = fields.Float(string="Quantity", default=1.0)
    price_unit = fields.Float(string="Price per unit")