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
        print("Good morning!")
        
    elif 12 <= hour < 18:
        print("Good afternoon")
        
    elif 18 <= hour < 21:
        print("Good evening!")
        
    else:
        print("Good night")

def chat():
    print("Welcome to ETE! Your AI friend is here to chat with you. 😊")
    print("Remember, you can end the session anytime by typing 'ok thanks for the session'.\n")