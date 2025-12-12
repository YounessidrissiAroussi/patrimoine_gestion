from odoo import models, fields, api

class Marque(models.Model):
    _name = 'patrimoine.marque'
    _description = 'Marque'

    libelle = fields.Char(string='Libellé', required=True)
