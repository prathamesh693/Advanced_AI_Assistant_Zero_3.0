import psutil
from FUNCTION.ZERO_SPEAK.speak import speak

def battery_percentage():
    battery = psutil.sensors_battery()
    percentage = int(battery.percent)

    speak(f"Battery percentage is {percentage} percent.")
        