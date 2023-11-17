import random
import json
import torch
from neuralnet import NeuralNet
from clap import Tester
from neurons import preprocess_text , tokenize
from task import NonInputFuncExe
from task import Openfunc
from whatsapp import WhatsappSender

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data :
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"] 

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Main Code ..........

Name = "Friday"
from listen import Listen
from speak import Speak

def Chatdata():
    sentence = Listen()

    if sentence == "bye":
        Speak("Fine , I am signing off for now...Don't think that u can relax yet .")
        exit()
    
    sentence = tokenize(sentence)
    sentence = ' '.join(sentence)  # Join tokens into a single string
    X = preprocess_text(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                reply = random.choice(intent["responses"])
                if "time" in reply :
                    Speak("Personally I think , Its high time for you to do something productive but for your convenience :")
                    NonInputFuncExe(reply)
                elif "date" in reply :
                    Speak("Swarnavo , are u alright ? You are asking a AI like me what is today's Date...come on dude people fear me for world dominition...")
                    NonInputFuncExe(reply)
                elif "day" in reply:
                    Speak("Well I have pretty concerned for your health but for your information today is :")
                    NonInputFuncExe(reply)
                elif "open" in reply:
                    Speak("As u wish swarnavo do u want me to open a website or an app from your laptop")
                    tasknew = Listen()
                    tasknew = str(tasknew).lower()
                    Openfunc(tasknew)
                elif "whatsapp" in reply:
                    Speak("Swarnavo who do u want to send the message ?")
                    Name = Listen()
                    Name = str(Name).lower()
                    Name = str(Name).replace("send ","")
                    Name = str(Name).replace("a ","")
                    Name = str(Name).replace("friday ","")
                    Name = str(Name).replace("whatsapp ","")
                    Name = str(Name).replace("message ","")
                    Name = str(Name).replace("to ","")
                    Name = str(Name).replace("my ","")
                    Name = str(Name).replace(" ","")
                    WhatsappSender(Name)
                    return True
                else:
                    Speak(reply)


def ClapDetection():
    query = Tester()
    if query == 'True-Mic':
        Speak("Welcome back Swarnavo , Access of Friday is granted to you ")


def Main():
    Chatdata()


if __name__ == '__main__':
    ClapDetection()
    while True:
        Main()





