import threading
from FUNCTION.ZERO_SPEAK.speak import speak
from BRAIN.MAIN_BRAIN.GOOGLE_BIG_DATA.google_big_data import *
from BRAIN.MAIN_BRAIN.GOOGLE_SMALL_DATA.google_small_data import *

def load_qa_data(file_path):
    qa_dict={}
    with open(file_path,"r",encoding="utf-8",errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts=line.split(":")
            if len(parts) != 2:
                continue
            q,a=parts
            qa_dict[q]=a
    return qa_dict

qa_file_path=r"R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\BRAIN_DATA\QNA_DATA\qna.txt"
qa_dict=load_qa_data(qa_file_path)

def brain_cmd(text):
    if "zero" in text:
        text = text.replace("zero", "")
        text=text.strip()
        if text in qa_dict:
            ans=qa_dict[text]
        elif "define" in text or "brief" in text or "research" in text or "teach me" in text:
            ans=deep_search(text)
        else:
            ans=search_brain(text)
            return ans

    else:
        pass



