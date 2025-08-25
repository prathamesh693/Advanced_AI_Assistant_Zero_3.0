from AUTOMATION.ZERO_BATTERY_AUTOMATION.BATTERY_PLUG_CHECK import battery_plug_check
from BRAIN.ACTIVITY.GREATINGS.WISH_GREATINGS.wish_greatings import Greating
from BRAIN.MAIN_BRAIN.BRAIN.brain import *
from AUTOMATION.MAIN_INTEGRATION._integration_automation import *
from FUNCTION.MAIN_FUNCTION_INTEGRATION.function_integration import *
from FUNCTION.ZERO_LISTEN.listen import *
from DATA.ZERO_DLG_DATASET.DLG import *
from BRAIN.ACTIVITY.GREATINGS.WELCOME_GREATINGS.welcome_greatings import *
from BRAIN.ACTIVITY.ADVICE.advice import *
from BRAIN.ACTIVITY.JOKE.jokes import *
from AUTOMATION.ZERO_BATTERY_AUTOMATION.BATTERY_PLUG_CHECK.battery_plug_check import *
from AUTOMATION.ZERO_BATTERY_AUTOMATION.BATTERY_ALERT.battery_alert import *
from playsound import playsound

def comain():
    while True:
        text = listen().lower()
        Automation(text)
        function_cmd(text)
        Greating(text)
        if text in goodbye_phrases:
            x=random.choice(goodbye_responses)
            speak(x)
            break
        elif  "zero" in text:
            response = brain_cmd(text)
            speak(response)
        else:
            pass

def main():
    playsound(r"R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\soundeffect\mixkit-unknown-technology-chirp-pattern-3125.wav")
    while True:
        wake_cmd = hearing().lower()
        if wake_cmd in wake_cmd:
            welcome()
            comain()
        else:
            pass

def zero():
    playsound(r"R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\soundeffect\mixkit-ui-zoom-out-2619.wav")
    t1= threading.Thread(target=main)
    t2= threading.Thread(target=battery_alert)
    t3= threading.Thread(target=check_plugin_status)
    t4= threading.Thread(target=advice)
    t5= threading.Thread(target=jokes)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


zero()