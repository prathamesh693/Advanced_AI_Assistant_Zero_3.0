import pywhatkit
import random
from DATA.ZERO_DLG_DATASET.DLG import search_result
from FUNCTION.ZERO_SPEAK.speak import speak

def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak(dlg)

#search_google("google")