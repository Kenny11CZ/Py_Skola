#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

class Window(gtk.Window):
	def __init__(self):
		super(Window, self).__init__()
		#Priprava hlavního okna
		self.set_size_request(200,50)
		self.set_title("Moje první okno")
		self.connect("destroy", gtk.main_quit)
		
		self.main_layout = gtk.VBox()
		#Vytvoření menu
		self.menu = gtk.MenuBar()
		#Vytvoření label (popisku)
		self.file_label = gtk.MenuItem("Soubor")
		#Připojení
		self.menu.append(self.file_label)
		
		#Vytvoření submenu
		self.file_menu = gtk.Menu()
		#Připojení submenu
		self.file_label.set_submenu(self.file_menu)
		
		self.close_label = gtk.MenuItem("Zavřít")
		self.reset_label = gtk.MenuItem("Resetovat")
		
		#Připojit zavření
		self.close_label.connect("activate", gtk.main_quit)
		self.reset_label.connect("activate", self.reset_stistknut)
		self.file_menu.append(self.close_label)
		self.file_menu.append(self.reset_label)
	
			
		self.main_layout.pack_start(self.menu, 0, 0, True);
		#Toolbar
		self.toolbar = gtk.Toolbar()
		self.toolbar.close = gtk.ToolButton(gtk.STOCK_CLOSE)
		self.toolbar.close.connect("clicked", gtk.main_quit)
		
		self.toolbar.reset = gtk.ToolButton(gtk.STOCK_DELETE)
		self.toolbar.reset.connect("clicked", self.reset_stistknut)
		
		self.toolbar.navys = gtk.ToolButton(gtk.STOCK_GOTO_TOP)
		self.toolbar.navys.connect("clicked", self.tlacitko_stisknuto)
		
		
		self.main_layout.pack_end(self.toolbar, 0, 0, True)
		
		self.toolbar.insert(self.toolbar.close, 0)
		self.toolbar.insert(self.toolbar.reset, 0)
		self.toolbar.insert(self.toolbar.navys, 0)
		
		self.tlacitko = gtk.Button("Zmackni me")
		self.tlacitko.connect("clicked", self.tlacitko_stisknuto)
		#self.pocitadlo = 0
		self.popisek = gtk.Label("0")
		
		self.layout = gtk.HBox()
		self.layout.pack_start(self.tlacitko, 0,0, True)
		self.layout.pack_end(self.popisek, 0, 0, True)
		
		self.main_layout.pack_end(self.layout, 0 , 0 ,True)
		
		self.add(self.main_layout)
		self.show_all()
		gtk.main()
		
	def tlacitko_stisknuto(self, widget):
		cislo = int(self.popisek.get_text())+1
		self.popisek.set_text(str(cislo))
		
	def reset_stistknut(self, widget):
		self.popisek.set_text("0")
		
				

Window()
