from FUNCTION.CHECK_INTERNET_SPEED.check_speed import *
from FUNCTION.CHECK_ONLINE_OFFLINE_STATUS.check_online_offline_status import  *
from FUNCTION.CHECK_TEMPERATURE.check_temperature import *
from FUNCTION.CLOCK.clock import *
from FUNCTION.FIND_MY_IP.find_my_ip import *
from FUNCTION.MUSIC_WITH_CLAP.clap_with_music import *

def function_cmd(text):
    if "check internet speed" in text or "check speed test" in text or "speed test" in text:
        check_internet_speed()
    elif "are you there" in text or "you are online" in text or "hello there" in text:
        internet_status()
    elif "check temperature" in text or "temperature" in text:
        Temp()
    elif "find my ip" in text or "ip address" in text or "my ip address" in text:
        speak("your IP is " + find_my_ip())
    elif "start clap with music" in text or "start smart music system" in text or "smart music system" in text:
        speak("ok now starting")
        clap_to_music()
    elif "what is time" in text or "time" in text or "what time is" in text:
        what_is_the_time()
    else:
        pass

# function_cmd("check internet speed")
#function_cmd("what is time")