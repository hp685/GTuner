#!/usr/bin/env python

from gi.repository import Gtk
import os
import sys

class Tuner(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="GuitarTuner")
        self.set_border_width(50)

        hbox = Gtk.Box(True,spacing=10,orientation=Gtk.Orientation.VERTICAL)
        self.add(hbox)


        """Low frequency E """
        button = Gtk.Button("E Low")
        button.connect("clicked", self.play)
        hbox.pack_start(button,True,True,0)

        """ A """
        button = Gtk.Button("A")
        button.connect("clicked",self.play)
        hbox.pack_start(button,True,True,0)

        """ D """
        button = Gtk.Button("D")
        button.connect("clicked",self.play)
        hbox.pack_start(button,True,True,0)

        """G"""
        button = Gtk.Button("G")
        button.connect("clicked",self.play)
        hbox.pack_start(button,True,True,0)

        """B"""
        button = Gtk.Button("B")
        button.connect("clicked",self.play)
        hbox.pack_start(button,True,True,0)

        """E"""
        button = Gtk.Button("E High")
        button.connect("clicked",self.play)
        hbox.pack_start(button,True,True,0)

    def play(self, button):
        """Switch according to the note selected"""
        if(button.get_label() == "E Low"):
            # Play E
            if(sys.platform.startswith('win')):
                winsound.beep(82.4, 7)
        elif (button.get_label() == "A"):
            if(sys.platform.startswith('win')):
                winsound.beep(110, 7)
        elif (button.get_label() == "D"):
            if(sys.platform.startswith('win')):
                winsound.beep(146.8, 7)
        elif (button.get_label() == "G"):
            if(sys.platform.startswith('win')):
                winsound.beep(196, 7)
        elif (button.get_label() == "B"):
            if(sys.platform.startswith('win')):
                winsound.beep(246.9, 7)
        elif (button.get_label() == "E High"):
            if(sys.platform.startswith('win')):
                winsound.beep(329.6, 7)






if __name__  == "__main__":
    win = Tuner()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
