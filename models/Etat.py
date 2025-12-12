from odoo import models, fields, api

class Etat(models.Model):
    _name = 'patrimoine.etat'
    _description = 'État'

    libelle = fields.Char(string='Libellé', required=True)
