import webbrowser
import wikipedia
from mood import (happy_list, sad_list, angry_list, depressed_list, suicidal_list,
                  happy_mood_responses, sad_mood_responses, angry_mood_responses,
                  depressed_mood_responses, suicidal_mood_responses, general_responses)
from functions import (speak_and_print, speak)

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
