import datetime

# Normal Time Function

def Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return time

# Date Function

def Date():
    date = datetime.date.today()
    return date

