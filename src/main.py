import pyttsx3
import speech_recognition as sr
from functions import (wishme, takecommand, speak_and_print)
from ete_utils import (is_assistant_task, handle_assistant_task, handle_therapist_mode)

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Adjust as per your preference

if __name__ == "__main__":
    wishme()
    while True:
        userInput = takecommand()
        if userInput == "None":
            continue  # Skip if no input detected

        # Check if the input is an assistant task
        if is_assistant_task(userInput):
            handle_assistant_task(userInput)
        elif "bye" in userInput or "close" in userInput:
            speak_and_print("Goodbye! Have a great day!")
            break
        elif "ok thanks for the session" in userInput:
            speak_and_print("Ok then, see you next time.")
            break
        else:
            handle_therapist_mode(userInput)
