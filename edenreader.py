#!/usr/bin/python

# Define imports
from gi.repository import Gtk

class EdenReader:

    def __init__(self):
        # Define our variables
        window = Gtk.Window();

        # Add eventhandlers
        window.connect("delete-event", Gtk.main_quit)

        # And don't forget to actually show the window
        window.show()

EdenReader()
Gtk.main()

