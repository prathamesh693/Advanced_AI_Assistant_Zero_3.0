import pyautogui
import time

# --- Basic Video Controls ---
def play_pause(): pyautogui.press('space')
def play_pause_alt(): pyautogui.press('k')
def mute_unmute(): pyautogui.press('m')
def fullscreen_toggle(): pyautogui.press('f')
def theater_mode_toggle(): pyautogui.press('t')
def miniplayer_toggle(): pyautogui.press('i')
def exit_fullscreen(): pyautogui.press('esc')
def toggle_subtitles(): pyautogui.press('c')

# --- Seeking & Navigation ---
def seek_back_5s(): pyautogui.press('left')
def seek_forward_5s(): pyautogui.press('right')
def seek_back_10s(): pyautogui.press('j')
def seek_forward_10s(): pyautogui.press('l')
def frame_back(): pyautogui.press(',')
def frame_forward(): pyautogui.press('.')
def seek_to(percent): pyautogui.press(str(percent))
def seek_start(): pyautogui.press('home')
def seek_end(): pyautogui.press('end')
def prev_chapter(): pyautogui.hotkey('ctrl', 'left')
def next_chapter(): pyautogui.hotkey('ctrl', 'right')

# --- Volume & Speed ---
def volume_up(): pyautogui.press('up')
def volume_down(): pyautogui.press('down')
def speed_down(): pyautogui.hotkey('shift', ',')
def speed_up(): pyautogui.hotkey('shift', '.')

# --- Playlist Navigation ---
def next_video(): pyautogui.hotkey('shift', 'n')
def previous_video(): pyautogui.hotkey('shift', 'p')

# --- Subtitles / Display Adjustments ---
def increase_font_size(): pyautogui.press('+')
def decrease_font_size(): pyautogui.press('-')
def rotate_text_opacity(): pyautogui.press('o')
def rotate_window_opacity(): pyautogui.press('w')

# --- Pan & Zoom ---
def pan_up(): pyautogui.press('w')
def pan_down(): pyautogui.press('s')
def pan_left(): pyautogui.press('a')
def pan_right(): pyautogui.press('d')
def zoom_in(): pyautogui.press(']')
def zoom_out(): pyautogui.press('[')

# --- Search & Navigation ---
def go_to_search(): pyautogui.press('/')
def tab_forward(): pyautogui.press('tab')
def tab_backward(): pyautogui.hotkey('shift', 'tab')
def activate_selected(): pyautogui.press('enter')  # or 'space' if needed
def close_settings(): pyautogui.press('esc')

# --- Fun Easter Egg ---
def toggle_party_mode():
    for char in "awesome":
        pyautogui.press(char)