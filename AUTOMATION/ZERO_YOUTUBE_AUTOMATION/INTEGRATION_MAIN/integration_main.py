from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.ANOTHER_AUTOMATION_IN_YOUTUBE.Another_Automation_in_youtube import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.CAPTION_IN_VIDEO.caption_in_video import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.MANUAL_SEARCH_ON_YOUTUBE.manual_search_on_youtube import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.PLAY_MUSIC_ON_YOUTUBE.play_music_on_Youtube import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.PLAY_PAUSE_VIDEO_ON_YOUTUBE.play_pause_video_on_youtube import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.SEARCH_ON_YOUTUBE.search_on_Youtube import *
from DATA.ZERO_DLG_DATASET.DLG import *
from FUNCTION.ZERO_LISTEN.listen import listen
from FUNCTION.ZERO_SPEAK.speak import speak


def youtube_cmd(text):
    if text in x:
        a = random.choice(q)
        speak(a)
        text = listen().lower()
        play_music_on_youtube(text)

    elif text in x1:
        stop()
    elif text in x2:
        play()

    elif text == "increase volume":
        volume_up()
    elif text == "decrease volume":
        volume_down()
    
    elif text == "seek forward 5 seconds":
        seek_forward_5s()
    elif text == "seek backward 5 seconds":
        seek_back_5s()

    elif text == "seek forward 10 seconds":
        seek_forward_10s()
    elif text == "seek backward 10 seconds":
        seek_back_10s()
    
    elif text == "seek backward frame":
        frame_back()
    elif text == "seek forward frame":
        frame_forward()

    elif text == "seek to start":
        seek_start()
    elif text == "seek to end":
        seek_end()

    elif text == "seek to previous chapter":
        prev_chapter()
    elif text == "seek to next chapter":
        next_chapter()

    elif text == "decrease playback speed":
        speed_down()
    elif text == "increase playback speed":
        speed_up()

    elif text == "next video":
        next_video()
    elif text == "previous video":
        previous_video()

    elif text == "toggle subtitles":
        toggle_subtitles()
    elif text == "toggle fullscreen":
        fullscreen_toggle()
    elif text == "toggle theater mode":
        theater_mode_toggle()   
    elif text == "toggle miniplayer":
        miniplayer_toggle()

    elif text == "exit fullscreen":
        exit_fullscreen()
    elif text == "toggle play pause":
        play_pause()
    elif text == "toggle play pause alternative":
        play_pause_alt()

    elif text == "toggle mute unmute":
        mute_unmute()

    elif text == "increase font size":
        increase_font_size()
    elif text == "decrease font size":
        decrease_font_size()

    elif text == "rotate text opacity":
        rotate_text_opacity()
    elif text == "rotate window opacity":
        rotate_window_opacity()
    
    elif text == "pan up":
        pan_up()
    elif text == "pan down":
        pan_down()

    elif text == "pan left":
        pan_left()
    elif text == "pan right":
        pan_right()

    elif text == "zoom in":
        zoom_in()
    elif text == "zoom out":
        zoom_out()

    elif text == "go to search":
        go_to_search()
    elif text == "tab forward":
        tab_forward()  
    elif text == "tab backward":
        tab_backward()
    
    elif text == "activate selected":
        activate_selected()
    elif text == "close settings":
        close_settings()
    elif text == "toggle party mode":
        toggle_party_mode()

    elif text.endswith("search in youtube"):
        text=text.replace("search in youtube", "")
        text = text.replace("search on youtube", "")
        youtube_search(text)

    elif text.endswith("search in current youtube window") or text.endswith("search on current youtube window") or text.endswith("search current youtube window") or text.startswith("search"):
        text = text.replace("search in current youtube window", "")
        text = text.replace("search", "")
        text = text.replace("search on current youtube window", "")
        text = text.replace("search current youtube window", "")
        search_manual(text)

    else:
        pass

#text="carry minati search in youtube"
#youtube_cmd(text)