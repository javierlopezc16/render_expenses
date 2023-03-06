# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    account_move_id =fields.Many2one('account.move', string='Factura')


class HrExpenseSheet(models.Model):
    _inherit = 'hr.expense.sheet'

    def invoice_payment(self):
        for line in self.expense_line_ids:
            if line.account_move_id:
                total_payment += line.total_amount

        # account_move = {
        #     'ref': 'Fondos por rendir',
        #     'date': fields.today(),
        #     'journal_id': 'Miscelaneous operations'
        # }
        #
        # lines = {
        #     'account_id':,
        #     'name':,
        #     'debit':,
        #     'credit':
        # }





