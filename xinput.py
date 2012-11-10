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

