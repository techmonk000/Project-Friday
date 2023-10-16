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
    Speak((day))

# --------Non Input Functions ---------

def NonInputFuncExe(query):

    query = str(query)

    if "time" in query:
        Time()
    
    if "date" in query:
        Date()
    if "day" in query:
        Day()
    



