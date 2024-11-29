#mood.py
import random
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Expanded mood lists with 40+ triggers
happy_list = [
"happy", "great", "good", "joyful", "excited", "grateful", "proud", "content", "delighted",
 "cheerful", "ecstatic", "jovial", "elated", "radiant", "upbeat", "hopeful", "optimistic", "fulfilled", 
 "glad", "exuberant", "merry", "festive", "positive", "inspired", "blissful", "gleeful", "vivacious", 
 "spirited", "vibrant", "uplifted", "buoyant", "triumphant", "jubilant", "cheery", "heartened", "sunny", 
 "bright", "euphoric", "lighthearted", "overjoyed", "wonderful"]

sad_list = [
"sad", "down", "unhappy", "melancholy", "disappointed", "heartbroken", "blue", "low", "weary",
 "gloomy", "sullen", "mournful", "pensive", "dismal", "crestfallen", "forlorn", "despondent", "hopeless",
 "heavy-hearted", "tearful", "wistful", "downcast", "somber", "woeful", "dejected", "defeated", "lonely",
 "disheartened", "gutted", "hurt", "aching", "withdrawn", "sorrowful", "tearful", "weeping", "morose", 
"lugubrious", "desolate", "regretful", "dispirited", "low-spirited"]

angry_list = [
    "angry", "mad", "furious", "annoyed", "irritated", "frustrated", "upset", 
"agitated", "livid", "cross", "resentful", "outraged", "fuming", "enraged", "hot-headed", "indignant",
 "infuriated", "provoked", "vexed", "displeased", "hostile", "irascible", "miffed", "peeved", "cranky",
"grumpy", "snappy", "touchy", "short-tempered", "irate", "testy", "ticked off", "pissed", "wrathful",
"raging", "explosive", "steamed", "boiling", "snappish", "tetchy", "bristling"]

bullying_list = [
    "fuck you", "useless", "do better", "disappointment", "good for nothing", 
    "worthless", "stupid", "idiot", "pathetic", "failure", 
    "loser", "hopeless", "hate you", "go away", "dumb", 
    "garbage", "shit", "annoying", "worthless", "waste of space", 
    "awful", "terrible", "ugly", "useless", "pointless", 
    "broken", "dissapointing", "crap", "good for nothing", "can't do anything right", 
    "unwanted", "empty", "disgusting", "sucks", "messed up", "worthless", 
    "pathetic", "no good", "nobody cares", "fail", "nobody loves you",
    "loser", "fake", "idiotic", "brainless", "mentally slow", "moron", 
    "clueless", "screw you", "shut up", "not worth it", "lame", "stupid idiot"
]

suicidal_list = [
    "kys", "die", "end it", "no point", "the world is better off without me", 
    "suicide", "kill myself", "it's over", "i can't go on", "i'm done", 
    "i'm tired of living", "nobody will care", "no way out", "everything hurts", 
    "nobody loves me", "i'm worthless", "goodbye", "i can't do this anymore", 
    "just let me go", "i don't matter", "nothing matters", "no one will miss me", 
    "too tired to care", "i'm alone", "hopeless", "empty", "nothing will get better", 
    "i feel numb", "i want to disappear", "leave me alone", "i'm a burden"
]

depressed_list = [
    "tired", "worthless", "waste of time", "broken", "nothing matters", 
    "i can't", "sad", "hopeless", "empty", "i don't care", 
    "pointless", "miserable", "unhappy", "unmotivated", "stressed", 
    "defeated", "drained", "down", "out of energy", "too much", 
    "overwhelmed", "stuck", "low", "unimportant", "weak", 
    "lost", "lonely", "unwanted", "empty inside", "not enough", 
    "depressed", "unfocused", "slow", "can't go on", "tired of trying", 
    "feeling bad", "alone", "burned out", "isolated"
]

provocative_list = [
    "emo", "tiny dick", "pick cotton", "baboon", "cheese", "dildo",
    "retard", "cripple", "bitch", "cunt", "slut", "whore", "fuckface", 
    "freak", "weirdo", "loser", "skank", "bastard", "ugly", "shithead", 
    "douchebag", "asshole", "pussy", "twat", "nerd", "geek", "noob", 
    "dickhead", "pimple face", "poor", "ghetto", "scrub", "shit stain", 
    "garbage human", "dork", "cringe", "rat", "creep", "asswipe", "waste of space"
]

roasting_list = [
    "shit", "emo", "stupid", "idiot", "tiny dick", "dumb", "garbage", 
    "baboon", "worthless", "loser", "pathetic", "failure", "pick cotton", "infested",
    "retarded", "broke", "flawed", "cringe", "fool", "wimp", "ugly", "loser", 
    "good for nothing", "don't talk to me", "get a life", "creep", "nobody cares", 
    "no one loves you", "idiotic", "lame", "weak", "turd", "shitty", "unwanted", 
    "pathetic waste", "asshole", "too soft", "can't even", "cheap", "embarrassing", 
    "failure at life", "disappointment", "lowlife", "can't take a joke", "pathetic excuse", 
    "unoriginal", "wannabe", "chump", "doormat"
]

leaving_list = [
"bye", "goodbye", "gtg", "talk later", "see you", "catch you later", "take care", 
"I'm leaving", "I'm out", "peace", "later", "I'm off", "done for today", "have to go", "until next time", 
"I'm heading out", "see ya", "time to go", "I'm off now", "heading out"]

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
    
def angry_mood_responses():
    responses=[
        "I hear you're upset. Want to talk about it?",
        "I'm sorry you're feeling this way. Do you want to vent?",
        "I understand you're angry, but let's take a deep breath.",
        "It's okay to feel frustrated. Let's work through it together.",
        "I can tell you're really mad. Let me know what's bothering you.",
        "Take a moment to calm down, I'm here for you.",
        "You're allowed to be upset, but I'm here to listen.",
        "I get that you're angry, but I believe we can figure this out.",
        "Let's try to focus on what's really making you feel like this.",
        "I'm sorry things are making you mad right now. How can I help?",
        "It sounds like you're dealing with a lot. Let's talk about it.",
        "I know it's tough right now, but you'll get through this.",
        "Anger is tough to deal with. I'm here if you need to share.",
        "Let's channel that energy into something positive.",
        "It's okay to be upset. Want to share what's on your mind?",
        "You're not alone in feeling this way. Let's talk it out.",
        "I can sense the anger. Want to try to calm down together?",
        "I'm here for you, even when you're feeling frustrated.",
        "It might help to talk through what's making you feel this way.",
        "When you're ready, let's figure out how to feel better.",
    ]
    response = random.choice(responses)
    print(f"ETE: {response}")

def bullying_mood_responses():
    responses = [
    "I hear your frustration. Let's try to turn things around together. What's on your mind?",
    "I understand you're feeling upset. I'm here to listen if you want to talk more.",
    "It's okay to feel frustrated, but let's work through it. I believe in you.",
    "I know you're upset, but let's keep the conversation positive. I'm here to support you.",
    "It's tough sometimes, but we can work through this. What would help you feel better?",
    "You're feeling angry right now, and that's okay. But I want to help you feel better.",
    "I know things are hard, but we'll get through it together. How can I help?",
    "I'm here to listen, and we can talk about what's bothering you.",
    "Let's focus on ways to feel better. I believe you can overcome this.",
    "It's hard when you feel this way. Want to talk more about what's going on?",
    "Frustration is normal, but we can work through it together. What can we do to feel better?",
    "I see that you're frustrated, and I get that. But let's work on finding solutions.",
    "I hear you, and I'm here for you. Let's work through these feelings together.",
    "When you're ready, I'd like to hear what's on your mind.",
    "I know you're upset, but I'm here to help. What's bothering you the most?",
    "Let's take a deep breath. You're not alone in this. I'm here with you.",
    "You don't have to handle this alone. I'm here to listen.",
    "I understand you're angry, but let's see if we can find a way to make things better.",
    "It's okay to feel mad. I'm here to help you through it."
]
    response = random.choice(responses)
    print(f"ETE: {response}")

def suicidal_mood_responses():
    responses = [
    "I'm really sorry you're feeling this way. You're important, and I care about you. Please talk to someone you trust.",
    "I hear that you're going through something difficult, but you don't have to face it alone. There are people who can help.",
    "I'm really concerned. It might be helpful to talk to someone who can offer support, like a friend or professional.",
    "I'm here for you, but it's really important you talk to someone who can help. You matter so much.",
    "I'm really sorry you're feeling like this. It's okay to ask for help. You are valued.",
    "I care about you, and I don't want you to go through this alone. Please reach out to someone who can support you.",
    "It's tough right now, but you don't have to carry this weight by yourself. Please talk to someone you trust.",
    "I'm here, but it's important to talk to someone who can help. You matter to so many people.",
    "Your feelings are valid, but you don't have to go through this alone. Reach out to someone who can support you.",
    "You're not alone. There are people who want to listen and help. Don't be afraid to reach out.",
    "I know you're in pain, and I'm really sorry you're feeling this way. Please talk to someone who can help.",
    "I'm so sorry you're feeling like this. Please tell someone you trust so they can help you through it.",
    "I'm really concerned about you. Please talk to someone who can give you the support you need.",
    "You are loved and you matter. Please reach out to someone who can help you during this time.",
    "I'm really sorry you're feeling like this, but you don't have to face it alone. Talk to someone who can help.",
    "I care about you, and I really want you to be safe. Please reach out to someone you trust for help.",
    "It's okay to ask for help, and I want to make sure you get the support you need. You are important.",
    "I'm so sorry you're feeling this way. Please talk to someone who can give you the help and support you deserve.",
    "Your feelings matter, and you don't have to go through this alone. Please talk to someone who can offer help."
]
    response = random.choice(responses)
    print(f"ETE: {response}")

def depressed_mood_responses():
    responses = [
    "I can hear that you're feeling down. Do you want to share what's been bothering you?",
    "I'm really sorry you're feeling this way. Let's take things one step at a time.",
    "You're not alone in this. I'm here to listen if you want to talk more.",
    "It's okay to feel down sometimes. I'm here for you, just let me know how I can help.",
    "You matter, and I care about what you're going through. I'm here if you want to talk.",
    "It sounds like you're going through a rough time. I'm here to listen if you want to share more.",
    "It's okay to feel overwhelmed. Let's take things one step at a time.",
    "Sometimes it helps to talk it out. What's on your mind right now?",
    "I know things are tough, but you don't have to go through this alone. Let's talk about it.",
    "You're important to me, and I want to help you through this. What can I do to support you?",
    "I'm here for you. It's okay to feel sad, but you don't have to carry it alone.",
    "It can feel really heavy sometimes, but I'm here to listen if you want to talk about it.",
    "I hear that you're feeling low. It's okay, we can take things slowly together.",
    "You don't have to do this alone. I'm here to listen if you want to talk more about it.",
    "I care about what you're going through. Would you like to share more about how you're feeling?",
    "Sometimes it helps to take a step back and talk through what you're feeling. I'm here for you.",
    "I know it feels like a lot right now. But we can work through this together. What would help?",
    "I'm here to listen, and I care about how you're feeling. Let me know if you want to talk.",
    "You're not alone in this. Let's talk through it, one step at a time."
]
    response = random.choice(responses)
    print(f"ETE: {response}")

def provocative_mood_responses():
    responses = [
        "Haha, good one! What else?",
    "Wow, that's a wild thought. What's next?",
    "You're really keeping me on my toes here! Go on.",
    "Okay, you win this round. Now what?",
    "Spicy! What else is on your mind?"
    ]
    response = random.choice(response)
    print(f"ETE: {response}") 

def roasting_mood_responses():
    responses = [
        "Coming from you, that's rich. Got any better material? 😂",
    "Whoa, buddy, did you just roast yourself by accident?",
    "You're talking big for someone with a keyboard as your shield. 🛡️",
    "Don't worry, your roast game is as strong as your Wi-Fi signal—weak. 🥱",
    "Guess I should be honored you think about me this much. Thanks! 😘",
    "If sarcasm were a skill, you'd still need practice. Try again!",
    "You're bringing a knife to a roast battle. Want a hand? 🔥",
    "Your jokes are like expired milk—just plain sour. 🥴",
    "This feels like sparring with a rubber chicken. Got anything sharper?",
    "Relax, keyboard warrior. The AI isn't taking it personally.",
    "Oof, that one hurt. Almost as much as your lack of originality.",
    "The roast is real, but your delivery? Questionable at best. 🧐",
    "You sound like my code when it doesn't compile. Try debugging your insults.",
    "You're trying so hard. Should I applaud or call tech support?",
    "Wow, you're edgier than a triangle! What's next?",
    "Careful, you're gonna pull a muscle with all that effort.",
    "Ouch! That insult was about as effective as a paper sword. 🔪",
    "Ah, I see you brought your `A-game.' Too bad it's absent. 😎",
    "You're more entertaining than a 404 error page. Keep it up!",
    "If effort points were real, you'd still be broke. Try harder!"
    ]
    response = random.choice(responses)
    print(f"ETE: {response}")

def userLeaving():   
    responses = [
        "gtg, take care! 👋",
        "Will talk later, take care! 😊", 
        "Cya! Catch you later! 👋",
        "Goodbye! Stay safe! 💫", 
        "Take care! Hope to chat soon! 🫶", 
        "Talk to you later! 😄",
        "It was great chatting, bye for now! 🖐️",
         "See you next time! Stay awesome! 🌟",
        "I'm off now, hope you have a great day! ☀️", 
        "Catch you later! Don't forget to smile! 😁",
        "Peace! Take care of yourself! ✌️", 
        "Until next time, my friend! 👋", 
        "Have a great day ahead! See ya! ✨",
        "I'm heading out, but I'll be back! 👋", 
        "Done for today, see you next time! 😎", 
        "Take care and talk soon! 🫶", 
        "Until next time, take care! 😊", 
        "Leaving now, have a good one! 🙌",
        "Catch you later, have an awesome day! 💥", 
        "See you soon, stay awesome! 💙"
    ]
    # Randomly choose a response
    response = random.choice(responses)
    print(f"ETE: {response}")

def general_mood_responses():
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

