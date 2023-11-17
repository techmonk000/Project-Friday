from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from speak import Speak
import pathlib
from listen import Listen

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "Database\\chromedriver.exe"
selenium_service = Service(PathofDriver)
driver = webdriver.Chrome(service=selenium_service,options=options)
driver.maximize_window()
wait = WebDriverWait(driver,30)
driver.get("https://web.whatsapp.com/")
sleep(15)
Speak("Swarnavo Whatsapp is ready now.....")

ListWeb = {'mrinmoy' : "+919836014691",
           'father': "+919831401246",
           'mother': '+917595948490',
           'raj':    '+919073740955'}

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = Listen()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        Speak("Message Sent")
        
    except:
        print("Invalid Number")

