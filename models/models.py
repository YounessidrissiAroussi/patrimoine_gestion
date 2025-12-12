# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TypeUnite(models.Model):
    _name = 'patrimoine.type.unite'
    _description = 'Type Unité'

    libelle = fields.Char(string='Libellé', required=True)


class Unite(models.Model):
    _name = 'patrimoine.unite'
    _description = 'Unité'

    code = fields.Char(string='Code', required=True)
    designation = fields.Char(string='Désignation', required=True)
    type_unite_id = fields.Many2one('patrimoine.type.unite', string='Type Unité')


class TypePatrimoine(models.Model):
    _name = 'patrimoine.type.patrimoine'
    _description = 'Type Patrimoine'

    libelle = fields.Char(string='Libellé', required=True)


class CategoriePersonnel(models.Model):
    _name = 'patrimoine.categorie.personnel'
    _description = 'Catégorie Personnel'

    libelle = fields.Char(string='Libellé', required=True)


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


class Etat(models.Model):
    _name = 'patrimoine.etat'
    _description = 'État'

    libelle = fields.Char(string='Libellé', required=True)


class EtatPatrimoineActif(models.Model):
    _name = 'patrimoine.etat.patri.actif'
    _description = 'État Patrimoine Actif'

    date_etat = fields.Date(string='Date État')
    etat_id = fields.Many2one('patrimoine.etat', string='État')
    patrimoine_actif_id = fields.Many2one('patrimoine.patrimoine.actif', string='Patrimoine Actif')


class Famille(models.Model):
    _name = 'patrimoine.famille'
    _description = 'Famille'

    libelle = fields.Char(string='Libellé', required=True)


class SousFamille(models.Model):
    _name = 'patrimoine.sous.famille'
    _description = 'Sous Famille'

    libelle = fields.Char(string='Libellé', required=True)
    famille_id = fields.Many2one('patrimoine.famille', string='Famille')


class Marque(models.Model):
    _name = 'patrimoine.marque'
    _description = 'Marque'

    libelle = fields.Char(string='Libellé', required=True)


class CategoriePatrimoineActif(models.Model):
    _name = 'patrimoine.categorie.patrim.actif'
    _description = 'Catégorie Patrimoine Actif'

    libelle = fields.Char(string='Libellé', required=True)


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
    
    # Relations
    patrimoine_geo_id = fields.Many2one('patrimoine.patrimoine.geographique', string='Patrimoine Géographique')
    unite_id = fields.Many2one('patrimoine.unite', string='Unité')
    categorie_patrim_actif_id = fields.Many2one('patrimoine.categorie.patrim.actif', string='Catégorie Patrimoine Actif')
    famille_id = fields.Many2one('patrimoine.famille', string='Famille')
    marque_id = fields.Many2one('patrimoine.marque', string='Marque')
    fournisseur_id = fields.Many2one('patrimoine.fournisseur', string='Fournisseur')
    
    # One2many
    etat_patri_actif_ids = fields.One2many('patrimoine.etat.patri.actif', 'patrimoine_actif_id', string='États')


# Module de gestion du Patrimoine
class GestionPatrimoine(models.AbstractModel):
    _name = 'patrimoine.gestion.patrimoine'
    _description = 'Module de gestion du Patrimoine'

    # Méthodes
    def package(self):
        pass

    def diagramme_diagramme_classe_1(self):
        pass

    def auteur_bj(self):
        pass

    def version(self):
        pass
