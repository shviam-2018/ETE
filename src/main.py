from functions import wishme, takecommand, speak_and_print, is_assistant_task, handle_assistant_task, handle_therapist_mode
def main():
    speak_and_print("Hello! I'm Thea. Would you like to talk or chat?")
    
    # Choose mode: 'talk' or 'chat'
    mode = input("Type 'talk' for voice input or 'chat' for text input: ").strip().lower()

    if mode not in ["talk", "chat"]:
        speak_and_print("Sorry, I didn't understand that. Please restart and choose 'talk' or 'chat'.")
        return

    wishme()
    
    while True:
        if mode == "talk":
            user_input = takecommand().lower()
        else:
            user_input = input("You: ").strip().lower()
        
        if user_input in ["exit", "quit"]:
            speak_and_print("Goodbye! Take care.")
            break
        
        if is_assistant_task(user_input):
            handle_assistant_task(user_input)
        else:
            handle_therapist_mode(user_input)

if __name__ == "__main__":
    main()
