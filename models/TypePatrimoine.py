from odoo import models, fields, api

class TypePatrimoine(models.Model):
    _name = 'patrimoine.type.patrimoine'
    _description = 'Type Patrimoine'

    libelle = fields.Char(string='Libellé', required=True)
