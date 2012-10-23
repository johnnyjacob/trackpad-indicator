#!/usr/bin/env python

import sys
import gtk
import appindicator

class Trackpad:
    def __init__(self):
        self.ind = appindicator.Indicator("trackpad-status-indicator",
                                           "indicator-messages",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        self.check_trackpad_status()
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def check_trackpad_status(self):
        trackpad_enabled = True
        if trackpad_enabled:
            self.ind.set_status(appindicator.STATUS_ATTENTION)
        else:
            self.ind.set_status(appindicator.STATUS_ACTIVE)
        return True

if __name__ == "__main__":
    indicator = CheckGMail()
    indicator.main()
