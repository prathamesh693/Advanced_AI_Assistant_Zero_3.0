import pyautogui as ui
from AUTOMATION.COMMON_AUTOMATION.COMMON_CLOSE.close import close
from AUTOMATION.COMMON_AUTOMATION.COMMON_OPEN.open import open

def common_cmd(text):
    if "open" in text or "kholo" in text:
        text = text.replace("open", "")
        text = text.replace("kholo", "")
        open(text)

    elif "close" in text or "band kar do" in text:
        text = text.replace("close", "")
        text = text.replace("band kar do", "")
        close()

    else:
        pass


#common_cmd("open youtube")