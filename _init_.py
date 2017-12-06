# -*- coding: utf-8 -*-
from . import crm

class Extension0(crm.lead):
    _name = 'extension.0'

    name = fields.Char(default="A")

class Extension1(mail.thread):
    _inherit = 'extension.0'

    description = fields.Char(default="Extended")
        env = self.env
        {'name': "A", 'description': "Extended"}
