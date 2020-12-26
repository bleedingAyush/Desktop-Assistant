import pyttsx3
from datetime import datetime
import speech_recognition as sr
import pyaudio
import wikipedia, os
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    """
    Function to wish me in the morning, afternoon and night
    """
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("Never give up Sir!")


def take_commmand():
    """
    It takes micorphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconginizing")
        query = r.recognize_google(audio, language="en-in")
        print("User said", query)
    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query

if __name__ == '__main__':
    wish_me()
    while True:
        query = take_commmand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("http://www.youtube.com")
        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("http://www.google.com")
        elif "time" in query:
            time = datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")
        elif "open chrome" in query:
            speak("Opening Chrome")
            chpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chpath)
        elif "open blender" in query:
            speak("Opening blender")
            bpath = "C:\\Program Files\\Blender Foundation\\Blender 2.91\\blender.exe"
            os.startfile(bpath)
        elif "sleep" in query:
            quit()
        elif "who are you" in query:
            speak("I am jarvis your virtual assistant.")
        elif "who is your father" in query:
            speak("My father is Mr. Ayush. He made me on 19th of December")
