from odoo import models, fields, api

class Famille(models.Model):
    _name = 'patrimoine.famille'
    _description = 'Famille'

    libelle = fields.Char(string='Libellé', required=True)
