import datetime
from FUNCTION.ZERO_SPEAK.speak import speak


def what_is_the_time():
    try:
        current_time=datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"The time is {current_time}")
    except Exception as e:
        error_message= f"An error has occured: {e}"
        print(error_message)
        speak(error_message)

#what_is_the_time()