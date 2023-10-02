import speech_recognition as sr # importing the speech_recognition library

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source: # using our own desktop microphone as source of voice
        print("Interpretaing and trying to analyse your voice ...")
        r.energy_threshold = 4000
        audio = r.listen(source,0,2.5) # making it such that after 2.5 seconds it stops listening to your voice

    try:
        print("Recognizing....")
        query = r.recognize_google(audio , language="en-in") # it is using google recogniser to catch the audio
        print(f"Sir, Your command was: {query}")

    except:
        return "There was an error ! "
    
    
    query = str(query)
    return query.lower() # it stores the command in lower case

Listen()
