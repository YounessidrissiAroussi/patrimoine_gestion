# -*- coding: utf-8 -*-
{
    'name': 'Gestion du Patrimoine',
    'version': '1.0',
    'category': 'Asset Management',
    'summary': 'Module de gestion du patrimoine géographique et actif',
    'description': """
        Module de Gestion du Patrimoine
        =================================
        
        Ce module permet de gérer:
        * Le patrimoine géographique (immeubles, étages, locaux)
        * Le patrimoine actif (équipements, matériels)
        * Les personnels et leurs catégories
        * Les fournisseurs
        * Les états et l'historique des patrimoines
        * Les familles et sous-familles de patrimoine
        * Les marques et les unités
        
        Auteur: BJ
        Version: 1.0
    """,
    'author': 'BJ',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
