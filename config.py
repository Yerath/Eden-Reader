#!/usr/bin/python

from os.path import expanduser

class EdenReaderConfig:

    def __init__(self):
        
        self.home = expanduser("~")

    def ReadMangaList(self):
        print self.home + "/.config/edenreader/mangalist"
        
