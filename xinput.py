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

import commands
import re

#Get the device id for touchpad

def xinput_set_device_state(deviceid, state):
    state_value = "0"
    if state == "on":
        state_value = "1"

    command = "xinput set-prop " + deviceid + " \"Device Enabled\" " + state_value
    print command
    commands.getoutput(command)

def xinput_get_deviceid(device):
    xinputresult = commands.getoutput('xinput')
    xinputlist = xinputresult.split('\n')

    #Parse and look for touchpad's device id
    for line in xinputlist:
        if re.search(device,line) :
            for id in re.findall(r'id=\d+\b',line):
                idlist = re.findall(r'\d+', id)
                touchpad_id = idlist[0]
    return touchpad_id

def xinput_get_enabled_status(deviceid):
    
    return "on"

deviceid = xinput_get_deviceid ("TouchPad")
xinput_set_device_state (deviceid, "off")

