# -*- coding: utf-8 -*-

from odoo import api, models, fields


class salesnotes(models.Model):
     _name = 'salesnotes.salesnotes'
     _inherit = ['mail.thread', 'mail.activity.mixin']     
   
     partner_id = fields.Many2one('res.partner', string='Customer')  
     salestype = fields.Selection([('visit', 'Visit'), ('phone call', 'Phone Call'), ('email', 'Email discussion'), ('tradeshow', 'TradeShow')], string='Type')
     salesdate = fields.Date(string='Date')
     salesnotes = fields.Char(string='Notes', required=True, track_visibility='onchange')
     salesperson = fields.Char(related='create_uid.name', string = "Salesperson", store=True)
#   
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
