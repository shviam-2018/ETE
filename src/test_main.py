import pytest
from unittest.mock import patch
import random
from your_module import wishme  # Adjust this import based on your code

def test_ete_conversation():
    # Mocking the input and print function
    with patch("builtins.input", side_effect=[
        "aaron",  # Simulating user entering their name
        "happy",  # Simulating user choosing a happy mood
        "sad",     # Simulating user choosing a sad mood
        "dilliga", # Simulating user typing a general word
        "mad",     # Simulating user choosing angry mood
        "gtg"      # Simulating user saying goodbye
    ]):
        with patch("builtins.print") as mocked_print, patch("random.choice") as mocked_random:
            # Mock the random.choice to return predictable values
            mocked_random.side_effect = [
                "You sound so excited; it's awesome!",  # happy response
                "I wish I could give you a real hug.",  # sad response
                "That sounds great! What's next?",  # general response
                "It's okay to be upset. Want to share what's on your mind?",  # angry response
                "Goodbye! Stay safe! 💫"  # goodbye response
            ]
    
            # Call the function that starts the conversation (ensure it's the correct function name)
            wishme()  # Adjust this to the actual function name in your code
    
            # Check that the greeting is printed
            mocked_print.assert_any_call("Good morning!")  # Change this to the actual greeting if it's different
            mocked_print.assert_any_call("Remember, you can end the session anytime by typing 'ok thanks for the session'.")
            mocked_print.assert_any_call("Hi aaron, how are you feeling today?")
    
            # Check that the responses are printed based on the mocked random choices
            mocked_print.assert_any_call("You sound so excited; it's awesome!")  # happy mood response
            mocked_print.assert_any_call("I wish I could give you a real hug.")  # sad mood response
            mocked_print.assert_any_call("That sounds great! What's next?")  # general response
            mocked_print.assert_any_call("It's okay to be upset. Want to share what's on your mind?")  # angry mood response
            mocked_print.assert_any_call("Goodbye! Stay safe! 💫")  # goodbye message

# Run the test
if __name__ == "__main__":
    pytest.main()
