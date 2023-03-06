# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    is_re_journal =fields.Boolean(string='Render Expense Journal')
