from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime


class AccountMove(models.Model):
    _inherit = "account.move"

    payment_date = fields.Date('Payment Date')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def reconcile(self):
        res = super(AccountMoveLine, self).reconcile()
        payment_date = None
        for rec in self:
            if rec.move_id.payment_id:
                payment_date = rec.move_id.payment_id.date
        for rec in self:
            if rec.move_id.move_type == 'out_invoice':
                rec.move_id.payment_date = payment_date
        return res

