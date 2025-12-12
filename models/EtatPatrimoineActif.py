from odoo import models, fields, api

class EtatPatrimoineActif(models.Model):
    _name = 'patrimoine.etat.patri.actif'
    _description = 'État Patrimoine Actif'

    date_etat = fields.Date(string='Date État')
    etat_id = fields.Many2one('patrimoine.etat', string='État')
    patrimoine_actif_id = fields.Many2one('patrimoine.patrimoine.actif', string='Patrimoine Actif')
