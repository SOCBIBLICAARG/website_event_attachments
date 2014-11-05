
from openerp import models, fields
#attachments_ids = fields.One2many('ir_attachments', 'res_id', string="Attachments")

class EventAttachments(models.Model):
	_inherit = 'event.event'
	attachment_ids = fields.One2many('ir.attachment', 'res_id', string="Attachments", copy=True)

