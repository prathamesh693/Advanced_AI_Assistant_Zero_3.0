import time
import random
import pywhatkit as kt
import pyautogui as ui
from FUNCTION.ZERO_SPEAK.speak import speak
from DATA.ZERO_DLG_DATASET.DLG import playsong

def play_music_on_youtube(text):
    playdlg = random.choice(playsong)
    speak(playdlg)
    kt.playonyt(text)
    time.sleep(3)
    playdlg = random.choice(playdlg)
    speak(playdlg+text)


# play_music_on_youtube("bal hanuman 2 movies")