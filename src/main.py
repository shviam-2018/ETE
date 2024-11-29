from functions import (wishme, chat)
from mood import ( happy_list, sad_list, happy_mood_responses, sad_mood_responses, general_responses)

wishme()
    
name = input("Please enter your name: ")
print(f"Hi {name}, how are you feeling today?\n")
    
while True:
        user_statement = input(f"{name}: ").lower()
        
        # Check user's statement against mood lists and provide responses
        if any(word in user_statement for word in happy_list):
            happy_mood_responses()
        elif any(word in user_statement for word in sad_list):
            sad_mood_responses()
        elif user_statement == "ok thanks for the session":
            print("ETE: Ok then, see you next time! Take care. 👋")
            break
        else:
            general_responses()

# Run the chat function
if __name__ == "__main__":
    chat()
