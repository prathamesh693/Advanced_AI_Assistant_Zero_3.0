import pyautogui
import time


# ====================
# ⬆ Scrolling (via shortcuts)
# ====================
def scroll_down():
    # Scroll down by pressing the Down arrow key
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')

def scroll_up():
    # Scroll up by pressing the Up arrow key
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')

def scroll_to_top():
    pyautogui.hotkey('home')

def scroll_to_bottom():
    pyautogui.hotkey('end')
