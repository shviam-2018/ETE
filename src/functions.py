#functions.py
import pyttsx3
import speech_recognition as sr
import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Function to speak the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to print a message and speak it
def speak_and_print(message):
    print(message)
    speak(message)

# Function to take microphone input and return string output
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

# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak_and_print("Good morning!")
        
    elif 12 <= hour < 18:
        speak_and_print("Good afternoon")
        
    elif 18 <= hour < 21:
        speak_and_print("Good evening!")
        
    else:
        speak_and_print("Good night")

# Function to check assistant tasks
def is_assistant_task(userInput):
    assistant_keywords = ["wikipedia", "youtube", "google", "email", "search", "news", "weather"]
    return any(word in userInput for word in assistant_keywords)

# Function to handle assistant tasks
def handle_assistant_task(userInput):
    if "wikipedia" in userInput:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(userInput.replace("wikipedia", ""), sentences=2)
        speak_and_print("According to Wikipedia")
        speak_and_print(results)
    elif "youtube" in userInput:
        webbrowser.open("https://www.youtube.com/")
    elif "google" in userInput:
        webbrowser.open("https://www.google.com/")
    elif "email" in userInput:
        webbrowser.open("https://mail.google.com/")
    elif "news" in userInput:
        webbrowser.open("https://www.bbc.com/news")
    elif "weather" in userInput:
        webbrowser.open("https://weather.com/")
    else:
        speak_and_print("I can't help with that task right now.")

# Function to handle therapist mode
def handle_therapist_mode(userInput):
    if any(word in userInput for word in happy_list):
        happy_mood_responses()
    elif any(word in userInput for word in sad_list):
        sad_mood_responses()
    elif any(word in userInput for word in angry_list):
        angry_mood_responses()
    elif any(word in userInput for word in depressed_list):
        depressed_mood_responses()
    elif any(word in userInput for word in suicidal_list):
        suicidal_mood_responses()
    else:
        general_responses()