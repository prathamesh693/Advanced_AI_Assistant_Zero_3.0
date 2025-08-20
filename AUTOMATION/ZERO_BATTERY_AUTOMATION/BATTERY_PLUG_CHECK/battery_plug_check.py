import psutil
import random
from DATA.ZERO_DLG_DATASET.DLG import plug_in,plug_out
from FUNCTION.ZERO_SPEAK.speak import speak


def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()
        
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                random_low = random.choice(plug_in)
                speak(random_low)
            else:
                random_low = random.choice(plug_in)
                speak(random_low)
            
        previous_state = battery.power_plugged


previous_state = None
plug_in1=["charger is plugged in check conform","battery is charging that means charger is plugged  check conformed."]
plug_out1=["charger is unplugged check conform","battery is not charging that means charger is unplugged check conformed."]

def check_plugin_status1():
    global previous_state

    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_low = random.choice(plug_in1)
            speak(random_low)
        else:
            random_low = random.choice(plug_out1)
            speak(random_low)
        
        previous_state = battery.power_plugged