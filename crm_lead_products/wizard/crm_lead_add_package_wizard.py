from odoo import models, fields


class CrmLeadAddPackageWizard(models.TransientModel):
    _name = "crm.lead.add.package.wizard"
    _description = "Wizard to add a product package to CRM Lead"

    package_id = fields.Many2one(
        "crm.lead.product.package",
        string="Product Package",
        required=True,
    )
    lead_id = fields.Many2one(
        "crm.lead",
        string="Lead",
        required=True,
    )

    def add_package(self):
        self.ensure_one()
        package_lines = self.package_id.product_ids
        lead_product_line_obj = self.env["crm.lead.product.line"]

        for line in package_lines:
            lead_product_line_obj.create({
                "lead_id": self.lead_id.id,
                "product_id": line.product_id.id,
                "product_quantity": line.product_quantity,
                "price_unit": line.price_unit,
                "description": line.product_id.name
            })
        return {"type": "ir.actions.act_window_close"}
