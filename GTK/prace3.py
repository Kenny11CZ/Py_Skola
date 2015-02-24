#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

class Dialog(gtk.Dialog):
	def __init__(self):
		super(Dialog, self).__init__()
		self.dialog = gtk.MessageDialog(type=gtk.MESSAGE_QUESTION, buttons=gtk.BUTTONS_OK_CANCEL)
		
		self.label = gtk.Label('YOLO')
		
		self.dialog.get_message_area().pack_start(self.label, 0, 0, True)
		
		
		
		self.area.pack_start(self.label, 0, 0, True)
		
		self.dialog.run();

Dialog()
