import random
from DATA.ZERO_DLG_DATASET.DLG import welcomedlg
from FUNCTION.ZERO_SPEAK.speak import speak

def welcome():
    welcome=random.choice(welcomedlg)
    speak(welcome)