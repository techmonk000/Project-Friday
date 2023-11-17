import datetime
from speak import Speak

def Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(time)

def Date():
    date = datetime.date.today()
    Speak(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak(day)

# --------Non Input Functions ---------

def NonInputFuncExe(query):

    query = str(query)

    if "time" in query:
        Time()

    if "date" in query:
        Date()
    if "day" in query:
        Day()

# -----Open functions------

import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def Openfunc(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        webname = Query.replace("visit", "").replace(" ", "")
        Link = f"https://www.{webname}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        webname = Query.replace("launch", "").replace(" ", "")
        Link = f"https://www.{webname}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        appname = Query.replace("open", "").replace(" ", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(appname)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "start" in Query:
        appname = Query.replace("start", "").replace(" ", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(appname)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True



