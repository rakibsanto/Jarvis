import pyttsx3 #pip install pyttsxc
import datetime
import speech_recognition as sr #pip install SpeechRecognition
engine= pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time(): 
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
time()
def date(): 
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme(): 
    speak("Welcome Back Sir!")
    speak("The Current time is")
    time()
    speak("The current date")
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12: 
        speak("Good morning Sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evining sir!")
    else: 
        speak("Good Night Sir!")

    speak("jarvis at your service please tell me how i help you sir!?")

def takeCommand(): 
    r= sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e: 
        print(e)
        speak("Say that again please..")
        return "None"
    return query
takeCommand()