import pyautogui as ui
import random
import time
from FUNCTION.ZERO_SPEAK.speak import speak
from DATA.ZERO_DLG_DATASET.DLG import s2, s1


def search_manual(text):
    ui.press("/")
    ui.write(text)
    s12 = random.choice(s1)
    speak(s12)
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12)

#time.sleep(2)
#search_manual("ajay devgan")
