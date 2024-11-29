#main.py
from functions import (wishme, chat)
from mood import ( happy_list, sad_list, angry_list, bullying_list, suicidal_list, depressed_list, provocative_list, roasting_list, 
leaving_list, happy_mood_responses, sad_mood_responses, angry_mood_responses, bullying_mood_responses, suicidal_mood_responses, 
depressed_mood_responses, provocative_mood_responses, roasting_mood_responses, userLeaving, general_mood_responses)

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

        elif any(word in user_statement for word in bullying_list):
             mood="bullying"
             print(f"[Detected Mood: {mood}]")
             bullying_mood_responses()

        elif any(word in user_statement for word in suicidal_list):
             mood="suicidal"
             print(f"[Detected Mood: {mood}]")
             suicidal_mood_responses()

        elif any(word in user_statement for word in depressed_list):
             mood="depressed"
             print(f"[Detected Mood: {mood}]")
             depressed_mood_responses()    

        elif any(word in user_statement for word in provocative_list):
               mood="provocative"
               print(f"[detected Mood: {mood}]")
               provocative_mood_responses()

        elif any(word in user_statement for word in roasting_list):
             mood="roasting"
             print(f"[Detected Mood: {mood}]")
             roasting_mood_responses()

        elif any(word in user_statement for word in leaving_list):
             mood="leaving"
             print(f"[Detected Mood: {mood}]")
             userLeaving()
             break
          
        else:
            mood = "General"
            print(f"[Detected Mood: {mood}]")
            general_mood_responses()


