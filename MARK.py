# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
import selenium
import pyttsx3
import pyaudio
import datetime
import sys
import pylint
import pyautogui
import psutil
import pyjokes
import smtplib
import os
import random
import wikipedia
import glob
import socket
import subprocess
import webbrowser as wb
from pygame import mixer
 
doss = os.getcwd()
i=0
n=0

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-4].id)

engine.say("welcome back sir!")
engine.runAndWait()

def assistant_speaks(audio):
    print('MARK II: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        assistant_speaks('Good Morning!')

    if currentH >= 12 and currentH < 18:
        assistant_speaks('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        assistant_speaks('Good Evening!')
  

greetMe()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    assistant_speaks("the current time is")
    assistant_speaks(Time)
time()

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    assistant_speaks(" and the date is")
    assistant_speaks(date)
    assistant_speaks(month)
    assistant_speaks(year)
date()

assistant_speaks("all drivers are updated and all functions are working properly.")
assistant_speaks("MARK II at your service sir!")
    
def get_audio(): 
  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing...")
        text = r.recognize_google(audio, language ='en-in') 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand PLease say that again !") 
        return 0
def process_text(): 
    if 'search' in str(text) or 'play' in str(text): 
        search_web(str(text)) 
        return 0


def jarvis(data):
    if "how are you" in data:
        assistant_speaks("I am fine")

    if "what time is it" in data:
        assistant_speaks(time())

def screenshot():
    img = pyautogui.screenshot()
    img.save("c:\\users\\hp\\Desktop\\jarvis\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    assistant_speaks('cpu is at'+ usage)

def jokes():
    assistant_speaks(pyjokes.get_joke())

def wifi():
    assistant_speaks('connecting')
  
# Driver Code 
if __name__ == "__main__": 
     
    while True: 
   
        text = get_audio().lower()

        if ('your name') in str(text):
            assistant_speaks('My name is MARK II, at your service sir')
  
        elif "time" in str(text):
            time()
        elif "date" in str(text):
            date()
        elif "hello" in str(text):
            assistant_speaks('Hello Sir')

        elif '.com' in str(text):
            assistant_speaks('Opening' + str(text))         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            wb.get(Chrome).open('http://www.'+str(text))
            print ('')
            
        elif 'jarvis' in str(text):
            assistant_speaks("Yes Sir?,What can I doo for you sir?")

        elif 'search in chrome' in str(text):
            assistant_speaks("what should i search here ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = get_audio().lower()
            wb.get(chromepath).open(search)

        elif "how are you" in str(text):
            assistant_speaks("I am fine")

        elif "what time is it" in str(text):
            assistant_speaks(time())

        elif "google maps" in str(text):
            query = str(text)
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            wb.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            assistant_speaks(result+'on google maps')
            
        elif str(text) != ('start music') and ('start') in str(text):   
            query = str(text)
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            assistant_speaks('starting '+result)

        elif str(text) != ('stop music') and ('stop') in str(text):
            query = str(text)
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            assistant_speaks('stopping '+result)

        elif('sleep') in str(text):
            assistant_speaks('good night')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')


        elif 'shutdown' in str(text):
            os.system("shutdown /s /t 1")

        elif 'restart' in str(text):
            os.system("shutdown /r /t 1")

        elif 'play some music' in str(text):
            songs_dir = 'D:\\music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember that' in str(text):
            assistant_speaks("what should i remember?")
            data = get_audio()
            assistant_speaks("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'you know that' in str(text):
            remember = open('data.txt','r')
            assistant_speaks("you said me to remember that"+remember.read())

        elif 'screenshot' in str(text):
            screenshot()
            assistant_speaks("done!sir.")

        elif 'cpu' in str(text):
            cpu()
            assistant_speaks("sir.")

        elif 'joke' in str(text):
            jokes()
            assistant_speaks("sir.")
        
        elif 'wi-fi' in str(text):  
            REMOTE_SERVER = "www.google.com"
            wifi()
            assistant_speaks('We are connected')
           

        elif 'music' in str(text):
            music = random.choice(glob.glob(doss + "D:\\music" + "\\*.mp3"))
            os.system('D:\\music')
            os.system('start ' + music)
            assistant_speaks('start playing')

        elif 'email' in str(text):
            assistant_speaks('Who is the recipient? ')
            recipient = get_audio()

            if 'me' in recipient:
                try:
                    assistant_speaks('tell me the email address of recipient')
                    content = get_audio()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("enter your email here", 'enter the password')
                    server.sendmail('rec. name', "rec. email id", content)
                    server.close()
                    assistant_speaks('Email sent!')

                except:
                    assistant_speaks('Sorry Sir! I am unable to send your message at this moment!')

        elif "who are you" in str(text) or "define yourself" in str(text): 
            speak = ('Hello, I am Your personal Assistant MARK II ,I am here to make your life easier.')
            assistant_speaks(speak) 
  
        elif "who made you" in str(text) or "created you" in str(text): 
            speak = "I have been created by ANURAG"
            assistant_speaks(speak)

            
        
  
        elif "exit" in str(text) or "bye" in str(text): 
            assistant_speaks("Yes sir, I think I was feeling a little tired. I'll take my leave now")
            assistant_speaks("disconnecting to the servers")
            quit()

       
def search_web(text): 
    driver = webdriver.Chrome() 
    driver.implicitly_wait(0) 
    driver.maximize_window() 
  
    if 'youtube' in str(text).lower(): 
  
        assistant_speaks("Opening in youtube") 
        indx = str(text).lower().split().index('youtube') 
        query = str(text).split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
  
    elif 'wikipedia' in str(text).lower(): 
  
        assistant_speaks("Opening Wikipedia") 
        indx = str(text).lower().split().index('wikipedia') 
        query = str(text).split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
  
    else: 
  
        if 'google' in str(text): 
  
            indx = str(text).lower().split().index('google') 
            query = str(text).split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in str(text): 
  
            indx = str(text).lower().split().index('google') 
            query = str(text).split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(str(text).split())) 
  
        return
  
  
# function used to open application 
# present inside the system. 
def open_application(input): 
  
    if "chrome" in str(text): 
        assistant_speaks("Google Chrome") 
        os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe') 
        return

    elif "vscode" in str(text) or "code" in str(text): 
        assistant_speaks("Opening vscode") 
        os.startfile('C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe') 
        return
  
    elif "word" in str(text): 
        assistant_speaks("Opening Microsoft Word") 
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE') 
        return
  
    elif "excel" in str(text): 
        assistant_speaks("Opening Microsoft Excel") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013.lnk') 
        return
    elif "Sublime" in str(text): 
        assistant_speaks("Opening Sublime Text") 
        os.startfile('C:\\Program Files\\Sublime Text 3\\sublime_text.exe') 
        return
    elif "Settings" in str(text): 
        assistant_speaks("Opening Settings") 
        os.startfile('%windir%\\System32\\Control.exe') 
        return
    elif "Adobe Photoshop" in str(text): 
        assistant_speaks("Opening Adobe Photoshop") 
        os.startfile('"C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe') 
        return
    elif "powerpoint" in str(text): 
        assistant_speaks("Opening Microsoft Powerpoint") 
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE') 
        return
    elif "onenote" in str(text): 
        assistant_speaks("Opening Microsoft onenote") 
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE') 
        return
    elif "cmd" in str(text): 
        assistant_speaks("Opening Command Prompt") 
        os.startfile('%windir%\\system32\\cmd.exe') 
        return
    elif "Control Panel" in str(text): 
        assistant_speaks("Opening Control Panel") 
        os.startfile('C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools') 
        return
    elif "This PC" in str(text): 
        assistant_speaks("Opening This PC") 
        os.startfile('C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools') 
        return
    elif "run" in str(text): 
        assistant_speaks("Opening run") 
        os.startfile('C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools') 
        return
    elif "notepad" in str(text): 
        assistant_speaks("Opening run") 
        os.startfile('%windir%\\system32\\notepad.exe') 
        return
    elif "notepad++" in str(text): 
        assistant_speaks("Opening notepad++") 
        os.startfile('C:\\Program Files\\Notepad++\\notepad++.exe') 
        return
    elif "microsoft edge" in str(text): 
        assistant_speaks("Opening microsoft edge") 
        os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application') 
        return
    elif "Dev C" in str(text): 
        assistant_speaks("Opening dev c++") 
        os.startfile('C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe') 
        return
    
    
    else: 
  
        assistant_speaks("Application not available") 
        return
