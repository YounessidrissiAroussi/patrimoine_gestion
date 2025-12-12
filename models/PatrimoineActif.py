from odoo import models, fields, api

class PatrimoineActif(models.Model):
    _name = 'patrimoine.patrimoine.actif'
    _description = 'Patrimoine Actif'

    code = fields.Char(string='Code', required=True)
    designation = fields.Char(string='Désignation', required=True)
    valeur_acquisition = fields.Char(string='Valeur Acquisition')
    date_acquisition = fields.Date(string='Date Acquisition')
    date_mise_service = fields.Date(string='Date Mise en Service')
    etat_actualite = fields.Char(string='État Actualité')
    n_bpc = fields.Char(string='N° BPC')
    n_bl = fields.Char(string='N° BL')
    n_facture = fields.Char(string='N° Facture')
    image_actif = fields.Binary(string='Image Actif')
    consigne_securite = fields.Char(string='Consigne Sécurité')
    degre_importance = fields.Char(string='Degré Importance')
    
    patrimoine_geo_id = fields.Many2one('patrimoine.patrimoine.geographique', string='Patrimoine Géographique')
    unite_id = fields.Many2one('patrimoine.unite', string='Unité')
    categorie_patrim_actif_id = fields.Many2one('patrimoine.categorie.patrim.actif', string='Catégorie Patrimoine Actif')
    famille_id = fields.Many2one('patrimoine.famille', string='Famille')
    marque_id = fields.Many2one('patrimoine.marque', string='Marque')
    fournisseur_id = fields.Many2one('patrimoine.fournisseur', string='Fournisseur')
    
    etat_patri_actif_ids = fields.One2many('patrimoine.etat.patri.actif', 'patrimoine_actif_id', string='États')
