# -*- coding: utf-8 -*-
{
    'name': "Fondos por Rendir",

    'summary': """
         Extensión del módulo de Gastos para gestiones Fondos por Rendir 
        """,

    'description': """
        Extensión del módulo de Gastos para gestiones Fondos por Rendir
    """,

    'author': "Javier López Castillo",

    'category': 'Human Resources/Expenses',
    'version': '0.1',

    'depends': [
        'hr_expense',
    ],

    'data': [
        'views/hr.expense.xml',
        'views/hr.expense.sheet.xml',
        'views/account.payment.view.re.xml',
        'views/account.journal.menu.xml',
        'views/account.journal.xml',
        'views/render.expenses.menu.xml',
    ],

}