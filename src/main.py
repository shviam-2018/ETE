#main.py
from functions import (wishme, chat)
from mood import ( happy_list, sad_list, angry_list, leaving_list, happy_mood_responses, sad_mood_responses, angry_mood_responses, userLeaving, general_responses)

mood = "NONE"

# Run the chat function
if __name__ == "__main__":
    chat()
    wishme()
    
name = input("Please enter your name: ")
print(f"Hi {name}, how are you feeling today?\n")
    
while True:
        user_statement = input(f"{name}: ").lower()
        
        # Check user's statement against mood lists and provide responses
        if any(word in user_statement for word in happy_list):
            mood = "Happy"
            print(f"[Detected Mood: {mood}]")
            happy_mood_responses()
            
        elif any(word in user_statement for word in sad_list):
            mood = "Sad"
            print(f"[Detected Mood: {mood}]")
            sad_mood_responses()

        elif any(word in user_statement for word in angry_list):
             mood="angry"
             print(f"[Detected Mood {mood}]")
             angry_mood_responses()
            
        elif any(word in user_statement for word in leaving_list):
             mood="leaving"
             print(f"[Detected mood: {mood}]")
             userLeaving()
             break

        else:
            mood = "General"
            print(f"[Detected Mood: {mood}]")
            general_responses()


