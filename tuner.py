#!/usr/bin/env python

from gi.repository import Gtk
import sys

try:
    import winsound
except ImportError:
    import os

def playsound(frequency, duration=10000):
    if(sys.platform.startswith('win')):
        winsound.beep(frequency, duration)
    elif(os.name == "posix"):
        os.system('beep -f %s -l %s' % (frequency, duration))

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
            playsound(82.4)
            print button.get_label()

        elif (button.get_label() == "A"):
            playsound(110)
            print button.get_label()

        elif (button.get_label() == "D"):
            playsound(146.8)
            print button.get_label()

        elif (button.get_label() == "G"):
            playsound(196)
            print button.get_label()

        elif (button.get_label() == "B"):
            playsound(246.9)
            print button.get_label()

        elif (button.get_label() == "E High"):
            playsound(329.6)
            print button.get_label()




if __name__  == "__main__":
    print "Beeps are 10s long"
    win = Tuner()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
    print "Happy Strumming!"
