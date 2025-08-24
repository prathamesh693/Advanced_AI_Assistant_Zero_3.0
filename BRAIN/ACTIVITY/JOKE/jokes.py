import random
import requests
from FUNCTION.ZERO_LISTEN.listen import listen
from FUNCTION.ZERO_SPEAK.speak import speak
import time


def get_random_joke():
    headers = {
        'Accept': 'application/json',
    }
    res=requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def jokes():
    while True:
        x=[600,550,580,400,3000,800,700,8200,8000,50,568]
        x=random.choice(x)
        time.sleep(x)
        speak("I have some joke for you, sir")
        text=listen().lower()
        if "yes tell me" in text or "yes" in text:
            advice =get_random_joke()
            speak(advice)
            pass
        else:
            speak("no problem sir, I just want to include some entertainment in your day")
            pass
#x=get_random_joke()
#print(x)