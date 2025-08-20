import pyautogui
import time


# ====================
# 🗂️ Tab and Window Management
# ====================

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')


# ====================
# 🔄 Page Navigation
# ====================

def refresh_page():
    pyautogui.hotkey('f5')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')


# ====================
# 🔍 Zoom & View
# ====================

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def toggle_full_screen():
    pyautogui.hotkey('f11')


# ====================
# 📁 Menus & Tools
# ====================

def open_browser_menu():
    pyautogui.hotkey('alt', 'e')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'shift', 'o')

def open_downloads():
    pyautogui.hotkey('ctrl', 'j')

def open_settings():
    pyautogui.hotkey('ctrl', 'l')          # Focus address bar
    time.sleep(0.5)
    pyautogui.write('chrome://settings/')  # Type the settings URL
    pyautogui.hotkey('enter')              # Press Enter
    

# ====================
# 🔄 Tab Switching
# ====================

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def reopen_closed_tab():
    pyautogui.hotkey('ctrl', 'shift', 't')
