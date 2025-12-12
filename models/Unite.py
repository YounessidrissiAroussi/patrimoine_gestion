from odoo import models, fields, api

class Unite(models.Model):
    _name = 'patrimoine.unite'
    _description = 'Unité'

    code = fields.Char(string='Code', required=True)
    designation = fields.Char(string='Désignation', required=True)
    type_unite_id = fields.Many2one('patrimoine.type.unite', string='Type Unité')
