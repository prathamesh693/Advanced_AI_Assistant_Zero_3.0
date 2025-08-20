import difflib
import webbrowser
import random
from DATA.ZERO_DLG_DATASET.DLG import websites, open_dld, open_maybe, success_open, sorry_open
from FUNCTION.ZERO_SPEAK.speak import speak

def openweb(text):

    # Convert the input to lowercase for case insensitive matching
    website_name_lower = text.lower()

    # Check if the exact website name exists in the dictionary
    if website_name_lower in websites:
        random_dlg = random.choice(open_dld)
        speak(random_dlg+text)
        url=websites[website_name_lower]
        webbrowser.open(url)
        randomsuccess = random.choice(success_open)
        speak(randomsuccess)
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            random_dlg = random.choice(open_dld)
            randomopen2 = random.choice(open_maybe)
            closest_match = matches[0]
            speak(randomopen2+random_dlg+text)
            url = websites[closest_match]
            webbrowser.open(url)
            randomsuccess = random.choice(success_open)
            speak(randomsuccess)
        else:
            randomsorry = random.choice(sorry_open)
            speak(randomsorry +" named "+ text)

#openweb("chatgpt")