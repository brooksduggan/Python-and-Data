# Test of voice recognition app - Leohnard
# Prototype 1, version 1

import speech_recognition as sr
import sys
import pyttsx3 as pyt
from bs4 import BeautifulSoup as bs
import requests


def getweather(city):
    url = "https://www.google.com/search?q=weather+{}".format(city)
    html = requests.get(url).content
    # create a new soup
    soup = bs(html, "html.parser")
    
    cur_location = soup.find("div", attrs={'id': 'wob_loc'})
    cur_temp = soup.find("div", attrs={'id': 'wob_tm'})
    
    response = "The current temperature in " + cur_location + " is " + cur_temp + " degrees."
    sys.stdout.write(response + "\n")
    sys.stdout.flush()
    return response
    


r = sr.Recognizer()

mic = sr.Microphone()

active = True
recording = ""
greeting = "Hello, my name is Leohnard.  How can I help you today?"
engine = pyt.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', voice_id)
engine.say(greeting)
engine.runAndWait()
sys.stdout.write(greeting + "\n")
sys.stdout.flush()

while active:
    response = ""
    
    try:
        with mic as source:
            audio = r.listen(source)

        script = r.recognize_google(audio)
        if "how are you" in script or "are you doing" in script:
            response = "I'm doing great!"
        elif "you are dumb" in script:
            response = "I may be dumb, but I am learning :)"
        if "temperature" in script or "weather" in script or "forecast" in script:
            city = script.split(" in ")[1]
            response = getweather(city)
        elif "greetings" in script or "hello" in script or "hey" in script or "hi" in script:
            response = "Hello, fine sir or madame!"
        elif "the gayest" in script:
            response = "Oh, that is Zack the-gay-man Goldstein."
        elif "solve this" in script or " + " in script or " - " in script or " * " in script or " / " in script:
            if " + " in script:
                res = [int(i) for i in script.split() if i.isdigit()]
                addition = res[0]+res[1]
                response = "The answer is " + str(addition)
            if " - " in script:
                res = [int(i) for i in script.split() if i.isdigit()]
                minus = res[0]-res[1]
                response = "The answer is " + str(minus)
            if " * " in script:
                res = [int(i) for i in script.split() if i.isdigit()]
                times = res[0]*res[1]
                response = "The answer is " + str(times)
            if " / " in script:
                res = [int(i) for i in script.split() if i.isdigit()]
                if res[1] == 0:
                    response = "You cannot divide by zero - undefined"
                else:
                    divided = res[0]/res[1]
                response = "The answer is " + str(divided)
        elif "goodbye" in script or "adios" in script:
            response = "Goodbye, friend! It was nice talking to you."
            engine.say(response)
            engine.runAndWait()
            sys.stdout.write(response + "\n")
            sys.stdout.flush()
            active = False
            break
        else:
            response = "I'm sorry, say again?"
            engine.say(response)
            engine.runAndWait()
            sys.stdout.write(response + "\n")
            sys.stdout.flush()
            
        engine.say(response)
        engine.runAndWait()
        sys.stdout.write(response + "\n")
        sys.stdout.flush()
        recording = recording + script + "\n"
    except:
        response = "Goodbye..."
        print(err)
        engine.say(response)
        engine.runAndWait()
        sys.stdout.write(response + "\n")
        sys.stdout.flush()
        break
print(recording)