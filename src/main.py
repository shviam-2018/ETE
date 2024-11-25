import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from mood import (happy_list, sad_list, angry_list, depressed_list, suicidal_list,
                  happy_mood_responses, sad_mood_responses, angry_mood_responses,
                  depressed_mood_responses, suicidal_mood_responses, general_responses)
from functions import (speak, speak_and_print, takecommand, wishme)

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Adjust as per your preference

if __name__ == "__main__":
    wishme()
    while True:
        userInput = takecommand()

        # Therapist Mode (Thea) logic
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
        elif "ok thanks for the session" in userInput:
            speak_and_print("Ok then, see you next time.")
            break
        # Assistant Mode (Emma) logic
        elif "wikipedia" in userInput:
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
        elif "bye" in userInput or "close" in userInput:
            speak_and_print("Goodbye! Have a great day!")
            break
        else:
            general_responses()
