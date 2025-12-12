from odoo import models, fields, api

class SousFamille(models.Model):
    _name = 'patrimoine.sous.famille'
    _description = 'Sous Famille'

    libelle = fields.Char(string='Libellé', required=True)
    famille_id = fields.Many2one('patrimoine.famille', string='Famille')
