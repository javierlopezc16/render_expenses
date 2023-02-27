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

    # any module necessary for this one to work correctly
    'depends': [
        'hr_expense',
    ],

    # always loaded
    'data': [
        'views/hr.expense.xml',
        'views/hr.expense.sheet.xml',
    ],
    # only loaded in demonstration mode

}