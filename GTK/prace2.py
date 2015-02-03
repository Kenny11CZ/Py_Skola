#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

class Window(gtk.Window):
	def __init__(self):
		super(Window, self).__init__()
		#Priprava hlavního okna
		self.set_size_request(200,50)
		self.set_title("Pridat jmeno")
		self.connect("destroy", gtk.main_quit)
		
		self.main_layout = gtk.VBox()
		
		self.napis = gtk.Label("Napis jmeno:")
		self.textbox = gtk.Entry()
		self.textbox.bind('<Entry>', self.pridat)
	
		
		self.main_layout.pack_start(self.napis, 0, 0, True);
		self.main_layout.pack_start(self.textbox, 0, 0, True);
		
		self.ok = gtk.Button("OK")
		self.ok.connect("clicked", self.pridat)
		self.cancel = gtk.Button("Cancel")
		self.cancel.connect("clicked", self.smazat)
		
		self.layout = gtk.HBox()
		self.layout.pack_start(self.cancel, 0,0, True)
		self.layout.pack_end(self.ok, 0, 0, True)
		
		self.main_layout.pack_end(self.layout, 0 , 0 ,True)
		
		self.add(self.main_layout)
		self.show_all()
		gtk.main()
		
		
	def pridat(self, widget):
		temp = self.textbox.get_text()
		f = open('test', 'a')
		f.write(temp)
		f.write("\n")
		self.textbox.set_text("")
		
	def smazat(self, widget):
		self.textbox.set_text("")

		
				

Window()
