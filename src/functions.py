# functions.py
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from mood import handle_mood_responses  # Import the generalized mood handler

# Initialize the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Core functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak_and_print(message):
    print(message)
    speak(message)

def takecommand():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        user_statement = r.recognize_google(audio, language="en-us")
        print(f"User side: {user_statement}\n")
    except Exception as e:
        speak_and_print("Say that again, please...")
        return "None"
    return user_statement

# Greet user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak_and_print("Good morning!")
    elif 12 <= hour < 18:
        speak_and_print("Good afternoon!")
    else:
        speak_and_print("Good evening!")

# Check if the user input relates to assistant tasks
def is_assistant_task(userInput):
    assistant_keywords = ["wikipedia", "youtube", "google", "email", "search", "news", "weather"]
    return any(word in userInput.lower() for word in assistant_keywords)

# Unified task handler
def handle_user_input(userInput):
    if is_assistant_task(userInput):
        handle_assistant_task(userInput)
    else:
        handle_mood_responses(userInput)

def handle_assistant_task(userInput):
    if "wikipedia" in userInput:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(userInput.replace("wikipedia", ""), sentences=2)
        speak_and_print("According to Wikipedia:")
        speak_and_print(results)
    elif "youtube" in userInput:
        webbrowser.open("https://www.youtube.com/")
    elif "google" in userInput:
        webbrowser.open("https://www.google.com/")
    # Add other assistant tasks here
    else:
        speak_and_print("I can't help with that task right now.")
