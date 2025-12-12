from odoo import models, fields, api

class CategoriePersonnel(models.Model):
    _name = 'patrimoine.categorie.personnel'
    _description = 'Catégorie Personnel'

    libelle = fields.Char(string='Libellé', required=True)
