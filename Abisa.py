import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 
# import serpapi
# from dotenv import load_dotenv

# load_dotenv()

# key = "64f0cfe33d85b1ed20b9e2eb510f2e45b6e42cbfbed9239500c88b8f8e5bbbbe"

# api_key = os.getenv('SERPAPI_KEY')
# client = serpapi.Client(api_key=key)
# location_basic = "Austin, Texas"

def talk(words):
    print(words)
    os.system("say " + words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    

talk("Hello, my name is Abisa, I will print whatever you will say, say open google to get to google. Say stop to stop") 

def command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=.2)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="en-EN").lower()
        print("You said: " + zadanie)
    except sr.UnknownValueError():
        talk("I did not understand")
        zadanie = command()
    return zadanie
        
def makeSomething(zadanie):
    google = 'https://google.com'
    if 'open google' in zadanie:
        talk("Opening")
        webbrowser.open(google)
    # elif 'search' in zadanie:
    #     search = zadanie
    #     result = client.search(
    #         q = search,
    #         engine = 'google',
    #         location = location_basic,
    #         hl = "en",
    #         gl = "us",
    #         )   
    elif 'stop' in zadanie:
        talk('Yes, sure')
        sys.exit()
    elif 'what is your name' in zadanie:
        talk("My name is Aalisa")
while True:
    makeSomething(command())

