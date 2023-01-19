import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import twilio
from twilio.rest import Client
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1 ].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("hey")
    speak("i am stella .")
    speak("Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Dharachoudhary2911@gmail.com', '*********')
    server.sendmail('dharachoudhary2911@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            # codePath = 
            # os.startfile(codePath)
            pass
        elif 'mood maker' in query:
            speak("starting System")
            speak("what would you like to do")
            if 'sad' in query:
                speak("screaching for the cheerful content on youtube")
                webbrowser.open("https://www.youtube.com")
                
        
        elif 'who developed you' in query:
            speak("i am a robot and i am devloped in python 3 and Dhara choudhary is the person who created me")
        elif 'play brown munde' in query:
            speak("playing brown munddee by AP DILLON")
            webbrowser.open("https://www.youtube.com/watch?v=VNs_cCtdbPc")
        elif 'manvendra singh' in query:
            speak("Dhara choudhary is the student of B.tech Computer Science Engineering studying in medicaps univrsity in indore and she is the person who has devloped me and she is the one who is involoved in diffrent tech .")
            if 'like' in query:
                pass       
        elif 'email ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak( "I am not able to send this email")
        elif 'shutdown' in query:
            speak("Shuting down ")
            speak("have a nice day sir")
            break        