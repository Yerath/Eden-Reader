#!/usr/bin/python

from gi.repository import Gtk

class EdenReaderWindow:

    def Create(self): # {{{

        self.window = Gtk.Window()
        self.grid   = Gtk.Grid()
        
        self.window.set_title("Eden Reader")

        # Bind eventhandlers
        self.window.connect("delete-event", Gtk.main_quit);

        # Create a grid to show stuff in
        #TODO: CREATE A LAYOUT

        self.window.add(self.grid)

        # Show the window
        self.window.show()

    # }}}

