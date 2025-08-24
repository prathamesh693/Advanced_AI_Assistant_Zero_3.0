from AUTOMATION.ZERO_AUTOMATION_GOOGLE.OPEN_WEBSITE.open_website import *
from AUTOMATION.ZERO_AUTOMATION_GOOGLE.SCROLL_ON_GOOGLE.scroll_automation import *
from AUTOMATION.ZERO_AUTOMATION_GOOGLE.SEARCH_ON_GOOGLE.search_on_google import *
from AUTOMATION.ZERO_AUTOMATION_GOOGLE.TAB_AUTOMATION.tab_automation import *
from AUTOMATION.COMMON_AUTOMATION.COMMON_OPEN.open import *

def google_cmd(text):
    if "open" in text:
        if "website" in text or "site" in text:
            text=text.replace("open","")
            text=text.replace("website","")
            text=text.replace("site","")
            text=text.strip()
            openweb(text)
        else:
            text=text.replace("open","")
            text=text.strip()
            if text =="":
               pass
            else:
                open(text)
    elif "scroll up" in text:
        scroll_up()

    elif "scroll down" in text:
        scroll_down()

    elif "scroll top" in text or "scroll to top" in text:
        scroll_to_top()

    elif "scroll bottom" in text or "scroll to bottom" in text:
        scroll_to_bottom()

    elif text.endswith("search in google"):
        text = text.replace("search in google", "")
        text = text.replace("search on google", "")
        search_google(text)

    elif "new tab" in text or "open tab" in text:
        open_new_tab()

    elif "close tab" in text or "remove tab" in text:
        close_tab()

    elif "private window" in text or "incognito" in text:
        open_private_window()

    elif "refresh" in text or "reload" in text:
        refresh_page()

    elif "go back" in text or "back page" in text:
        go_back()

    elif "go forward" in text or "next page" in text:
        go_forward()

    elif "zoom in" in text or "increase zoom" in text:
        zoom_in()

    elif "zoom out" in text or "decrease zoom" in text:
        zoom_out()

    elif "full screen" in text or "toggle full screen" in text:
        toggle_full_screen()

    elif "menu" in text or "open menu" in text:
        open_browser_menu()

    elif "developer tools" in text or "inspect" in text:
        open_dev_tools()

    elif "history" in text or "open history" in text:
        open_history()

    elif "bookmarks" in text or "open bookmarks" in text:
        open_bookmarks()

    elif "download" in text or "downloads" in text or "open downloads" in text:
        open_downloads()

    elif "settings" in text or "open settings" in text:
        open_settings()

    elif "next tab" in text or "switch tab" in text:
        switch_to_next_tab()

    elif "previous tab" in text or "back tab" in text:
        switch_to_previous_tab()

    elif "reopen tab" in text or "restore tab" in text:
        reopen_closed_tab()

    else:
        pass

#text="jay hanuman search in google"
#google_cmd(text)