#!/usr/bin/python

# Define imports
import gtk

class EdenReader:

    def Close(self, widget):
        gtk.main_quit()
    
    def __init__(self):
        # Define our variables
        window = gtk.Window();

        # Add eventhandlers
        window.connect("destroy", self.Close)

        # And don't forget to actually show the window
        window.show()

EdenReader()
gtk.main()

