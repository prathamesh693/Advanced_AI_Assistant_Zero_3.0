import psutil
import random
import time
from DATA.ZERO_DLG_DATASET.DLG import low_b, mid_b, high_b, full_b
from FUNCTION.ZERO_SPEAK.speak import speak

def battery_alert():
    while True:
        time.sleep(10)  # Check every 10 seconds
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)

        if percentage<20:
            random_low = random.choice(low_b)
            speak(random_low)
        
        elif percentage<50:
            random_mid = random.choice(mid_b)
            speak(random_mid)
        
        elif percentage<80:
            random_high = random.choice(high_b)
            speak(random_high)
        
        elif percentage>=80:
            random_full = random.choice(full_b)
            speak(random_full)
        
        else:
            pass

        time.sleep(1500)  # Wait for 25 minutes before checking again


def battery_alert1():
    battery = psutil.sensors_battery()
    percentage = int(battery.percent)

    if percentage<20:
        random_low = random.choice(low_b)
        speak(random_low)
        
    elif percentage<50:
        random_mid = random.choice(mid_b)
        speak(random_mid)
        
    elif percentage<80:
        random_high = random.choice(high_b)
        speak(random_high)
        
    elif percentage>=80:
        random_full = random.choice(full_b)
        speak(random_full)
        
    else:
        speak("sir, your battery is in perfect condition")