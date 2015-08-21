from openerp import models
from openerp import fields
from openerp import api


class hr_holidays_status(models.Model):
    _inherit = "hr.holidays.status"

    uom = fields.Many2one(
        'product.uom',
        string='Unit of Measure',
        default=lambda self: self.env.ref("product.product_uom_day"))


class hr_holidays(models.Model):
    _inherit = "hr.holidays"

    @api.depends('holiday_status_id')
    def _compute_uom(self):
        if self.holiday_status_id and self.holiday_status_id.uom:
            self.uom = self.holiday_status_id.uom
        else:
            self.uom = self.env.ref("product.product_uom_day")

    @api.depends('duration')
    def _compute_number_of_days_temp(self):
        days = self.uom._compute_qty_obj(
            from_unit=self.uom,
            qty=self.duration,
            to_unit=self.env.ref("product.product_uom_day"))
        self.number_of_days_temp = days

    uom = fields.Many2one(
        'product.uom',
        compute=_compute_uom,
        string='Unit of Measure')

    duration = fields.Float(
        'Allocation',
        readonly=True,
        states={'draft':[('readonly',False)], 'confirm':[('readonly',False)]}, copy=False)

    number_of_days_temp = fields.Float(
        'Allocation',
        readonly=True,
        compute=_compute_number_of_days_temp,
        store=True,
        states={'draft':[('readonly',False)], 'confirm':[('readonly',False)]}, copy=False)
