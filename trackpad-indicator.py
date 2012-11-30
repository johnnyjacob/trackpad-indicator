#!/usr/bin/env python

# Copyright (C) 2012 Johnny Jacob <johnnyjacob@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import gtk
import appindicator
from xinput import xinput

class Trackpad:
    def __init__(self):
        self.input_manager = xinput()
        self.ind = appindicator.Indicator("trackpad-status-indicator",
                                           "touchpad-active",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("touchpad-disabled")

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.tpad_item = gtk.MenuItem("TouchPad Off")
        self.tpad_item.connect("activate", self.set_touchpad_status)
        self.tpad_item.show()
        self.menu.append(self.tpad_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def set_touchpad_status (self, widget):
        status = self.input_manager.get_enabled_status ("TouchPad")
        if status == "off":
            self.ind.set_status(appindicator.STATUS_ACTIVE)
            self.input_manager.set_device_state ("TouchPad", "1")
            self.tpad_item.set_label("TouchPad off")
        else:
            self.ind.set_status(appindicator.STATUS_ATTENTION)
            self.input_manager.set_device_state ("TouchPad", "0")
            self.tpad_item.set_label("TouchPad on")
        
    def main(self):
        self.check_touchpad_status()
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def check_touchpad_status(self):
        status = self.input_manager.get_enabled_status ("TouchPad")
        if status == "off":
            self.ind.set_status(appindicator.STATUS_ATTENTION)
            self.tpad_item.set_label("TouchPad on")
        else:
            self.ind.set_status(appindicator.STATUS_ACTIVE)
            self.tpad_item.set_label("TouchPad off")

        return True

    def touchpad_on(state):
        self.input_manager.set_device_state("TouchPad", "1")

    def touchpad_off(state):
        self.input_manager.set_device_state("TouchPad", "0")


    def get_touchpad_deviceid():
        xinputresult = commands.getoutput('xinput')
        xinputlist = xinputresult.split('\n')

        #Parse and look for touchpad's device id
        for line in xinputlist:
            if re.search("TouchPad",line) :
                for id in re.findall(r'id=\d+\b',line):
                    idlist = re.findall(r'\d+', id)
                    touchpad_id = idlist[0]
                    return touchpad_id

if __name__ == "__main__":
    indicator = Trackpad()
    indicator.main()
