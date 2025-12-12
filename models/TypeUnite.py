from odoo import models, fields, api

class TypeUnite(models.Model):
    _name = 'patrimoine.type.unite'
    _description = 'Type Unité'

    libelle = fields.Char(string='Libellé', required=True)
