from odoo import models, fields, api

class Fournisseur(models.Model):
    _name = 'patrimoine.fournisseur'
    _description = 'Fournisseur'

    code = fields.Char(string='Code', required=True)
    denomination = fields.Char(string='Dénomination', required=True)
    adresse = fields.Char(string='Adresse')
    tel = fields.Char(string='Téléphone')
    fax = fields.Char(string='Fax')
    email = fields.Char(string='Email')
    nom_resp = fields.Char(string='Nom Responsable')
    prenom_resp = fields.Char(string='Prénom Responsable')
    gsm1 = fields.Char(string='GSM1')
    gsm2 = fields.Char(string='GSM2')
