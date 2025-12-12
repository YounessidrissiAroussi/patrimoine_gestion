from odoo import models, fields, api

class Personnel(models.Model):
    _name = 'patrimoine.personnel'
    _description = 'Personnel'

    matricule = fields.Char(string='Matricule', required=True)
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    fonction = fields.Char(string='Fonction')
    tel = fields.Char(string='Téléphone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')
    categorie_personnel_id = fields.Many2one('patrimoine.categorie.personnel', string='Catégorie Personnel')
