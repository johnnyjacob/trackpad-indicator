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

        self.tpad_item = gtk.MenuItem("Trackpad off")
        self.tpad_item.connect("activate", self.quit)
        self.tpad_item.show()
        self.menu.append(self.tpad_item)

    def main(self):
        self.check_trackpad_status()
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def check_trackpad_status(self):
        trackpad_enabled = False
        if trackpad_enabled:
            self.ind.set_status(appindicator.STATUS_ATTENTION)
        else:
            self.ind.set_status(appindicator.STATUS_ACTIVE)
        return True

    def touchpad_on(deviceid, state):
        state_value = "0"
        if state == "on":
            state_value = "1"

        command = "xinput set-prop " + deviceid + " \"Device Enabled\" " + state_value
        print command
        commands.getoutput(command)

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
