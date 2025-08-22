import requests
from FUNCTION.ZERO_SPEAK.speak import speak


def get_random_joke():
    headers = {
        'Accept': 'application/json',
    }
    res=requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

#x=get_random_joke()
#print(x)