#!/usr/bin/python

# {{{ Define imports
from gi.repository import Gtk
from config import EdenReaderConfig
# }}}

class EdenReader:

    def __init__(self): # {{{
        self.CreateWindow()
    # }}}

    def CreateWindow(self): # {{{
        print "Create the main window"

        window = Gtk.Window();

        # Set eventhandlers
        window.connect("delete-event", Gtk.main_quit)

        # Set some generic info on the window
        window.set_title("Eden Reader")

        # Show the window
        window.show()

    # }}}

EdenReader()

# Get into the GTK loop
Gtk.main()

