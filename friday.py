import random
import json
import torch
from neuralnet import NeuralNet
from clap import Tester
from neurons import preprocess_text , tokenize

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






