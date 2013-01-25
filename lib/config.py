#!/usr/bin/python

from os.path import expanduser

class EdenReaderConfig:

    def __init__(self): # {{{
        
        self.home = expanduser("~")
        self.location = {
            "mangalist": self.home + "/.config/edenreader/mangalist"
        }

    # }}}

    def ReadMangaList(self): # {{{
        print "Reading " + self.location["mangalist"]

        conf = [line.strip() for line in open(self.location["mangalist"])]

    # }}}
        
