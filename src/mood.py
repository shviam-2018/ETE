import random
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Expanded mood lists with 40+ triggers
happy_list = ["happy", "great", "good", "joyful", "excited", "grateful", "proud", "content", "delighted", "cheerful", "ecstatic", "jovial", "elated", "radiant", "upbeat", "hopeful", "optimistic", "fulfilled", "glad", "exuberant", "merry", "festive", "positive", "inspired", "blissful", "gleeful", "vivacious", "spirited", "vibrant", "uplifted", "buoyant", "triumphant", "jubilant", "cheery", "heartened", "sunny", "bright", "euphoric", "lighthearted", "overjoyed", "wonderful"]

sad_list = ["sad", "down", "unhappy", "melancholy", "disappointed", "heartbroken", "blue", "low", "weary", "gloomy", "sullen", "mournful", "pensive", "dismal", "crestfallen", "forlorn", "despondent", "hopeless", "heavy-hearted", "tearful", "wistful", "downcast", "somber", "woeful", "dejected", "defeated", "lonely", "disheartened", "gutted", "hurt", "aching", "withdrawn", "sorrowful", "tearful", "weeping", "morose", "lugubrious", "desolate", "regretful", "dispirited", "low-spirited"]

angry_list = ["angry", "mad", "furious", "annoyed", "irritated", "frustrated", "upset", "agitated", "livid", "cross", "resentful", "outraged", "fuming", "enraged", "hot-headed", "indignant", "infuriated", "provoked", "vexed", "displeased", "hostile", "irascible", "miffed", "peeved", "cranky", "grumpy", "snappy", "touchy", "short-tempered", "irate", "testy", "ticked off", "pissed", "wrathful", "raging", "explosive", "steamed", "boiling", "snappish", "tetchy", "bristling"]

# Friendlier responses with 20+ variations
def happy_mood_responses():
    responses = [
        "That's awesome! Tell me more!",
        "Wow, that sounds amazing!",
        "I'm so happy to hear that!",
        "You totally deserve this joy!",
        "Let's celebrate! 🎉",
        "Your happiness is contagious!",
        "Keep shining, superstar!",
        "Good vibes all around!",
        "That made my day too!",
        "You're radiating positivity!",
        "I love hearing that!",
        "High five! 🙌",
        "You're on a roll!",
        "Tell me more about what made you smile.",
        "That's the spirit! Keep it up!",
        "You sound so excited; it's awesome!",
        "Life's better with moments like these.",
        "Your joy is my joy!",
        "I'm all ears for more good news.",
        "What a fantastic moment to share!"
    ]
    response = random.choice(responses)
    print(f"ETE: {response}")
    

def sad_mood_responses():
    responses = [
        "I'm here for you. Want to talk more?",
        "Hey, it's okay to feel down sometimes.",
        "I get it. Rough days happen. Let's get through it together.",
        "I'm sending you a big virtual hug.",
        "You're stronger than you think. Let's chat.",
        "It's okay to not be okay. I'm with you.",
        "Do you want to share what's on your mind?",
        "I'm really sorry you're feeling this way.",
        "Let's find a little light in this together.",
        "You matter, and your feelings matter too.",
        "I'm listening; take your time.",
        "I wish I could give you a real hug.",
        "It's tough, but I know you can handle this.",
        "I believe in you. You've got this.",
        "You're not alone; I'm here for you.",
        "Want to talk about something that makes you happy?",
        "I care about you, no matter what.",
        "Your feelings are valid. Let's work through them.",
        "Even on cloudy days, you're not alone.",
        "Let's get through this together, step by step."
    ]
    response = random.choice(responses)
    print(f"ETE: {response}")
    

def general_responses():
    responses=[
        "That's interesting! Tell me more. 😊",
    "Hmm, I see. What else is on your mind?",
    "I'm here to listen, go ahead. 🌟",
    "That's cool! Do you have any other thoughts to share?",
    "I understand. How does that make you feel?",
    "Wow, really? Tell me more about it!",
    "I'm all ears. What else would you like to discuss?",
    "That sounds great! What's next?",
    "I'm glad we're having this chat. What's on your mind?",
    "That's something worth talking about! Keep going.",
    "I love hearing your thoughts! Share more.",
    "Interesting perspective! How do you feel about it?",
    "Let's dive deeper. What are your thoughts on that?",
    "Your insights are fascinating! Want to elaborate?",
    "I'm here for you. What else would you like to say?",
    "That's a good point! What made you think of that?",
    "I appreciate you sharing this with me. 😊",
    "That's really thoughtful. Any other ideas?",
    "Keep going, I'm really enjoying our chat!",
    "I like how you think! What else is on your mind?"
    ]
    response = random.choice(responses)
    print(f"ETE: {response}")