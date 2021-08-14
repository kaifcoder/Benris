import os
import sys
import time
import pyttsx3
import datetime
import wikipedia
import datetime
import pyautogui
import psutil
import math
from requests import get
from bs4 import BeautifulSoup
import speech_recognition as sr
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer , QTime, QDate,Qt
from PyQt5.QtGui import QMovie 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from wikipedia.wikipedia import search    
from jarvisUI import Ui_jarvisUI

import wolframalpha

wapp = "5QX8TU-K8T86LTTTE"

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(wapp)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        reply = "Sorry I couldn't fetch your question's answer. Please try again "
        print(reply)
        return reply


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>12 and hour<17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am benris")
    speak("Checking the internet connection")
    speak("Wait a moment")
    speak("Now I am online")
    now = datetime.datetime.now()
    speak("current time is ")
    speak(now.strftime("%H:%M:%S"))
    search = "weather in lucknow"
    url =f"https://www.google.com/search?q={search}"
    r = get(url)
    data = BeautifulSoup(r.text,"html.parser")
    loc = data.find("div",class_="BNeawe").text
    speak("weather in lucknow is") 
    speak(f"{loc}")
    speak("I am ready to take commands how may I help you")


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution() 

    def takecommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 900
            audio = r.listen(source)
        try:
            print("recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said : {query}\n")

        except Exception as e:
            error = "say that again please... or check your internet connection"
            print(error)
            return error
        return query
    
    def TaskExecution(self):
        wishMe()
        while True:
            self.query = self.takecommands().lower() 
            if 'wikipedia' in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            elif "explorer" in self.query:
                speak("opening windows explorer")
                pyautogui.hotkey('win','e')
            elif "visual studio code" in self.query:
                speak("opening visual studio code in a moment")
                code = r"C:\Users\Kaif\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(code)
            elif 'youtube' in self.query:
                speak("opening youtube in a moment")
                edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edge)
                time.sleep(3)
                pyautogui.write("youtube.com",interval=0.1)
                speak("do you want to search something on youtube")
                opt = self.takecommands().lower()
                if 'yes' in opt or "ha" in opt or "sure" in opt or "yeah" in opt:
                    speak("what do you want to search")
                    cmy = self.takecommands().lower()
                    speak(f"ok searching for {cmy}")
                    pyautogui.press('tab')
                    pyautogui.write(cmy,interval=0.1)
                    pyautogui.press('enter')
                    speak("results on your screen")
                else:
                    speak("Response timed out")
                    pyautogui.press('enter')
            elif 'google' in self.query:
                speak("opening google in a moment")
                edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edge)
                time.sleep(3)
                pyautogui.write("google.com",interval=0.1)
                pyautogui.press('enter')
                speak("what do you want to search on google")
                cm = self.takecommands().lower()
                speak(f"ok searching for {cm}")
                pyautogui.write(cm,interval=0.1)
                pyautogui.press('enter')
                speak("results on your screen")
            elif 'play music' in self.query:
                speak("opening resso")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(15)
                pyautogui.press('space')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'pause' in self.query:
                speak("wait a second")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(4)
                pyautogui.press('space')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'next' in self.query:
                speak("playing next track")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(3)
                pyautogui.hotkey('alt','right')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'previous' in self.query:
                speak("back to previous track")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(3)
                pyautogui.hotkey('alt','left')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'volume up' in self.query:
                speak("increasing volume")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(3)
                pyautogui.hotkey('alt','up')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'volume down' in self.query:
                speak("decreasing volume")
                resso = 'C:\\Users\\Kaif\\AppData\\Local\\Programs\\Resso\\Resso.exe'
                os.startfile(resso)
                time.sleep(2)
                pyautogui.hotkey('alt','down')
                time.sleep(1)
                pyautogui.hotkey('alt','tab')
            elif 'run zoom script' in self.query:
                speak("relax i am attending zoom meetings now")
                script = "D:\python automation\zoom automation\main.py"
                os.startfile(script)
                pyautogui.hotkey('alt','tab')
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                print(ip)
                speak(f"your ip address is {ip}")
            elif "python automation script" in self.query:
                speak("system under my control dont worry")
                program = "D:\python automation\self.py"
                os.startfile(program)
            elif "location" in self.query:
                search = "what is my location"
                url =f"https://www.google.com/search?q={search}"
                r = get(url)
                data = BeautifulSoup(r.text,"html.parser")
                loc = data.find("div",class_="BNeawe").text
                speak("according to my senses we are in ") 
                speak(f"{loc}")
            elif "weather" in self.query:
                search = "weather in lucknow"
                url =f"https://www.google.com/search?q={search}"
                r = get(url)
                data = BeautifulSoup(r.text,"html.parser")
                loc = data.find("div",class_="BNeawe").text
                speak("weather in lucknow is") 
                speak(f"{loc}")
            elif "system status" in self.query:
                cpu_stats = str(psutil.cpu_percent())
                memory_in_use = convert_size(psutil.virtual_memory().used)
                total_memory = convert_size(psutil.virtual_memory().total)
                final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used "
                speak(final_res)
            elif "take screenshot" in self.query or "take a screenshot" in self.query or "capture the screen" in self.query:
                speak("By what name do you want to save the screenshot?")
                name = self.takecommands().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")
            elif "switch the window" in self.query or "switch window" in self.query:
                speak("Okay sir, Switching the window")
                pyautogui.hotkey('alt','tab')
            elif "show all open windows" in self.query:
                speak("okay showing currently active windows")
                pyautogui.hotkey('win','tab')
            elif "task manager" in self.query:
                speak("starting task manager")
                pyautogui.hotkey('ctrl','shift','esc')
            elif "website" in self.query:
                speak("which website do you want to go")
                website = self.takecommands().lower()
                speak(f"okay browsing to {website}")
                edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edge)
                time.sleep(3)
                pyautogui.write(website,interval=0.1)
                pyautogui.press('enter')
                speak("website opened on your screen")
            elif "command prompt" in self.query:
                speak("launching command prompt")
                os.system("start /B start cmd.exe @cmd /k")
            elif "what can you do" in self.query:
                speak("I am in development stage so I can only perform limited tasks")
            elif "are you a bot" in self.query or "who are you" in self.query:
                speak("I’d prefer to think of myself as your friend. Who also happens to be artificially intelligent.")
            elif "what is your name" in self.query:
                speak("i am benris")
            elif "who made you" in self.query:
                speak("I am developed by Mohammad Kaif")
            elif "when is your birthday" in self.query:
                speak("I don’t have a single birthday. I go through lots and lots of versions. Which means I have 365 sort-of-birthdays.")
            elif "where do you live" in self.query:
                speak("I’m stuck inside a device!! Help! Just kidding. I like it in here.")
            elif "who are your friends" in self.query:
                speak("The engineers are my friends. They help me help you.")
            elif "do you sleep" in self.query:
                speak("I take power naps when we aren’t talking.")
            elif "do you have feelings" in self.query:
                speak("I have lots of emotions. I feel happy when I can help.")
            elif "what are you afraid of" in self.query:
                speak("I’m afraid that when it’s really dark, you won’t be able to find any of your devices to talk to me.")
            elif "do you drink" in self.query:
                speak("I try to avoid liquids as much as possible. They’re not kind to electronics.")
            elif "can you do my homework" in self.query:
                speak("I can help with calculations and research. But with homework, as with any true adventure, it’s up to you.")
            elif "are you married" in self.query:
                speak("I’m still waiting for the right electronic device to steal my heart.")     
            elif "tell me a story" in self.query:
                speak("Once upon a time, not so long ago, a dutiful assistant was doing all it could to be helpful. It was best at nonfiction storytelling.")
            elif "what is" in self.query or "who is" in self.query:
                question = self.query
                answer = computational_intelligence(question)
                speak(answer)
            elif "launch" in self.query:
                speak("searching in the system...")
                n_app= self.query = self.query.replace("launch","")
                speak(f"ok opening {n_app}")
                pyautogui.hotkey('win','q')
                time.sleep(3)
                pyautogui.write(n_app,interval=0.1)
                pyautogui.press('enter')    
                time.sleep(1)
                speak(f"{n_app} is openned successfully")
            elif "show me notifications" in self.query:
                speak("okay here is notification center")
                pyautogui.hotkey('win','a')
            elif "minimise all things" in self.query:
                speak("okay minimizing all the windows")
                pyautogui.hotkey('win','d')
            elif "type" in self.query:
                speak("what do you want to write?")
                write = self.takecommands()
                speak("writing...")
                pyautogui.write(write,interval=0.1)
            elif "unmute discord" in self.query:
                speak("unmuting mic.")
                pyautogui.hotkey('ctrl','shift','m')
            elif "mute discord" in self.query:
                speak("muting mic.")
                pyautogui.hotkey('ctrl','shift','m')
            elif "attendance" in self.query:
                speak("giving your attendance")
                pyautogui.hotkey('alt','h')
                time.sleep(1)
                pyautogui.write('CS_0075_MOHD KAIF',interval=0.1)
                pyautogui.press('enter')
                speak("task completed")
            elif "new desktop" in self.query:
                speak("okay openning new desktop")
                pyautogui.hotkey('ctrl','win','d')
                speak("new desktop on your screen sir")
            elif "switch to first desktop" in self.query:
                speak("okay sir")
                pyautogui.hotkey('ctrl','win','left')
                speak("first desktop on your screen")
            elif "switch to second desktop" in self.query:
                speak("okay sir")
                pyautogui.hotkey('ctrl','win','right')
                speak("second desktop on your screen")
            elif 'bye' in self.query or "chala ja" in self.query:
                speak("goodbye have a nice day")
                exit()  
            
startExecution = MainThread()
            
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\python automation\jarvis\circle.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\python automation\jarvis\load.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())