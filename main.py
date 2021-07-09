import pyttsx3 as p
import googletrans
import english
import hindi
import tkinter as tk
from tkinter import *
import os
import speech_recognition as sr
import GUI

gt = googletrans.Translator()

r = sr.Recognizer()

engine = p.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate' , 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#new code
#root = tk.Tk()

#T = tk.Text(root, height = 52, width = 100, bg="#b8beff")
#T.pack()

#root.title('Linux Voice Assistant')
##

while True:

    GUI.root.update_idletasks()
    GUI.root.update()

    language = "Continue with English or switch to Hindi? "
    GUI.shortener("\nLINUX VA: " + language)
    speak(language)

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        GUI.shortener("\n\nUSER: " + text)
        print(text)
        text = text.lower()

    if "english" in text :
        GUI.shortener("\n\nLINUX VA: Continuing with English")
        english.wish()
        while True:
            english.assistant()
    elif "hindi" in text:
        output = "Switching to Hindi"
        GUI.shortener("\n\nLINUX VA: " + output)
        hindi.wish()
        while True:
            hindi.assistant()