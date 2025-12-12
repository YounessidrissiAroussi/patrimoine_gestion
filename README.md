# Module Odoo - Gestion du Patrimoine

## Description

Ce module Odoo permet de gérer le patrimoine géographique et actif d'une organisation.

### Fonctionnalités principales:

1. **Patrimoine Géographique**
   - Gestion des immeubles, étages et locaux
   - Stockage de fiches techniques (immeuble, étage, local)
   - Croquis et plans

2. **Patrimoine Actif**
   - Gestion des équipements et matériels
   - Suivi des acquisitions (date, valeur, fournisseur)
   - Historique des états
   - Images et documentation

3. **Personnel**
   - Gestion du personnel
   - Catégorisation
   - Assignation en tant que responsable de patrimoine

4. **Configuration**
   - Types de patrimoine
   - Unités et types d'unités
   - Familles et sous-familles
   - Marques
   - États
   - Catégories

5. **Fournisseurs**
   - Coordonnées complètes
   - Contacts responsables

## Installation

### 1. Structure du module

```
patrimoine_gestion/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── models.py
├── views/
│   ├── views.xml
│   └── menu.xml
└── security/
    └── ir.model.access.csv
```

### 2. Installation dans Odoo

1. Copiez le dossier `patrimoine_gestion` dans le répertoire `addons` de votre installation Odoo:
   ```bash
   cp -r patrimoine_gestion /path/to/odoo/addons/
   ```

2. Redémarrez le serveur Odoo:
   ```bash
   sudo service odoo restart
   ```
   ou
   ```bash
   ./odoo-bin -c /path/to/odoo.conf
   ```

3. Activez le mode développeur dans Odoo:
   - Paramètres → Activer le mode développeur

4. Mettez à jour la liste des applications:
   - Applications → Mettre à jour la liste des applications

5. Recherchez "Gestion du Patrimoine" et cliquez sur Installer

## Utilisation

### Menu principal

Le module ajoute un menu principal "Patrimoine" avec deux sous-sections:

1. **Gestion**
   - Personnel
   - Patrimoine Géographique
   - Patrimoine Actif
   - Historique États

2. **Configuration**
   - Catégories Personnel
   - Types Patrimoine
   - Catégories Patrimoine Actif
   - Unités
   - Types Unité
   - Familles
   - Sous-Familles
   - Marques
   - Fournisseurs
   - États

### Workflow recommandé

1. **Configuration initiale**
   - Créer les types d'unités
   - Créer les unités
   - Créer les types de patrimoine
   - Créer les catégories de personnel
   - Créer les états possibles
   - Créer les familles et sous-familles
   - Créer les marques

2. **Gestion du personnel**
   - Enregistrer le personnel
   - Assigner les catégories

3. **Patrimoine géographique**
   - Créer les patrimoines géographiques (immeubles, étages, locaux)
   - Assigner les responsables
   - Uploader les fiches techniques

4. **Patrimoine actif**
   - Enregistrer les fournisseurs
   - Créer les patrimoines actifs
   - Lier aux patrimoines géographiques
   - Suivre l'historique des états

## Auteur

**BJ**

Diagramme de classes: Diagramme Classe 1

## Version

1.0

## Licence

LGPL-3
