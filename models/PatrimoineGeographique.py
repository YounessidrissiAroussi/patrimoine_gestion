from odoo import models, fields, api

class PatrimoineGeographique(models.Model):
    _name = 'patrimoine.patrimoine.geographique'
    _description = 'Patrimoine Géographique'

    code = fields.Char(string='Code', required=True)
    designation = fields.Char(string='Désignation', required=True)
    croquis = fields.Char(string='Croquis')
    fiche_immeuble = fields.Binary(string='Fiche Immeuble')
    fiche_etage = fields.Binary(string='Fiche Étage')
    fiche_local = fields.Binary(string='Fiche Local')
    type_patrimoine_id = fields.Many2one('patrimoine.type.patrimoine', string='Type Patrimoine')
    unite_id = fields.Many2one('patrimoine.unite', string='Unité')
    responsable_id = fields.Many2one('patrimoine.personnel', string='Responsable')
