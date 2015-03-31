#!/usr/bin/env python
# -*- coding: utf-8 -*-



import gtk

class Window(gtk.Window):
	def __init__(self):
		#Window definitions
		super(Window, self).__init__()
		self.set_size_request(400,400)
		self.connect("destroy", gtk.main_quit)
		
		#Define elements
		self.layout = gtk.VBox()
		self.toolbar = gtk.Toolbar()
		self.add_new = gtk.ToolButton()
		self.add_new.set_label("Přidat")
		self.add_new.set_icon_name("document-new")
		self.add_new.connect("clicked", self.on_add_new_clicked)
		self.toolbar.insert(self.add_new,0)
		#odebiraci tlacitko
		#list-remove	
		self.rem = gtk.ToolButton()
		self.rem.set_label("Odebrat")
		self.rem.set_icon_name("list-remove")
		self.rem.connect("clicked", self.on_rem_clicked)
		self.toolbar.insert(self.rem,1)
		self.treeview = gtk.TreeView()
					# First name, last name
		self.model = gtk.TreeStore(str,str)
		jmena = [
			["Karel","Omacka"],
			["Josef","Hnizdo"],
			["Tomas","Maly"],
			["Blanka","Protrhla"]
		]
		#Pro kazdy prvek v poli jmen dosadit do modelu
		for prvek in jmena:
			self.model.append(None,prvek)
		#Setting data for treeview
		self.treeview.set_model(self.model)
		sloupce = ["Jmeno","Prijmeni"]
		renderer = gtk.CellRendererText()
		#Pripojeni sloupcu
		pozice=0
		for i in sloupce:
			tmp = gtk.TreeViewColumn(i, renderer, text=pozice)
			self.treeview.append_column(tmp)
			pozice+=1
		
		
		
		
		
		#Packing
		self.layout.pack_start(self.toolbar, expand=False)
		self.layout.pack_start(self.treeview)
		self.add(self.layout);
		self.show_all()
	def on_add_new_clicked(self, widget):
		dialog = gtk.MessageDialog(message_format = "Zadej jméno", buttons=gtk.BUTTONS_OK_CANCEL)
		dialog.vstup = gtk.Entry()
		dialog.get_content_area().pack_start(dialog.vstup)
		
		dialog.vstup.show()
		res = dialog.run()
		if(res == gtk.RESPONSE_OK):
			self.model.append(None,dialog.vstup.get_text().split(" "))
		
		dialog.destroy()
		
		
	def on_rem_clicked(self, widget):
		(pozice, pozice) =  self.treeview.get_selection().get_selected()
		print self.model.get_value(pozice, 0)
		print self.model.get_value(pozice, 1)
		self.model.remove(pozice)
		
		
		
Window()
gtk.main()
