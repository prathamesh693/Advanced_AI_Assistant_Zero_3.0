import pyautogui
import time

def pause_play():
    pyautogui.press('space')

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_back_5s():
    pyautogui.press('left')

def seek_forward_5s():
    pyautogui.press('right')

def seek_back_10s():
    pyautogui.press('j')

def seek_forward_10s():
    pyautogui.press('l')

def frame_back():
    pyautogui.press(',')

def frame_forward():
    pyautogui.press('.')

def seek_to(percent):  # percent is an int 0–9
    if 0 <= percent <= 9:
        pyautogui.press(str(percent))

def seek_start():
    pyautogui.press('home')  # ↖ Home key

def seek_end():
    pyautogui.press('end')

def prev_chapter():
    pyautogui.hotkey('ctrl', 'left')

def next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def speed_down():
    pyautogui.hotkey('shift', ',')

def speed_up():
    pyautogui.hotkey('shift', '.')

def next_video():
    pyautogui.hotkey('shift', 'n')

def previous_video():
    pyautogui.hotkey('shift', 'p')

