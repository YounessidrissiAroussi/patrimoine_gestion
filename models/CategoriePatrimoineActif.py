from odoo import models, fields, api

class CategoriePatrimoineActif(models.Model):
    _name = 'patrimoine.categorie.patrim.actif'
    _description = 'Catégorie Patrimoine Actif'

    libelle = fields.Char(string='Libellé', required=True)
