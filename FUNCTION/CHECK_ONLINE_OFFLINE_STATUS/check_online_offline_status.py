import requests
from FUNCTION.OFFLINE_VOICE.speak2 import fspeak
from FUNCTION.ZERO_SPEAK.speak import speak


def is_online(url="https://www.google.com",timeout=5):
    try:
        # Try to make a GET request to the specified URL
        response = requests.get(url, timeout=timeout)
        #Check if the respose status code is in the success range (200-299)
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False

# Example usage
def internet_status():
    if is_online():
        x="Yes sir! I am ready and online"
        speak(x)
    else:
        x="Hey there sir! I am Female AI, Sorry Zero is not online"
        print(x)



