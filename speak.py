from gtts import gTTS # importing the gtts package 
import os
import time 
def say(text, lang='en'): # creating a function for the ai to talk
    try:
        tts = gTTS(text=text, lang=lang) 
        tts.save("output.mp3")
        time.sleep(1)
        os.system("mpg123 output.mp3")  # storing the output voice as a mp3 file
        os.remove("output.mp3")
        print("  ")
        print(f"Friday: {text}")# printing the speech said by ariel to make it easier to understand
        print("  ")
    except Exception as e:
        print(f"An error has occurred: {e}")

# Build by Swarnavo Mukherjee . This is the start of the project