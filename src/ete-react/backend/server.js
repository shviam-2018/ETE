const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors()); // Enable CORS for frontend to communicate with the backend
app.use(express.json()); // To parse incoming JSON data

// Define lists of mood-triggering words
const happyList = ['happy', 'joy', 'excited', 'good', 'great'];
const sadList = ['sad', 'down', 'unhappy', 'depressed'];
const angryList = ['angry', 'mad', 'rage', 'furious'];
const bullyingList = ['bullied', 'harassed', 'abused'];
const suicidalList = ['suicidal', 'end it', 'take my life'];
const depressedList = ['depressed', 'hopeless', 'lost'];
const provocativeList = ['stupid', 'idiot', 'dumb'];
const roastingList = ['roast', 'burn', 'joke'];
const leavingList = ['goodbye', 'see you', 'bye'];

// Define response functions for each mood
function happyMoodResponse() {
  return "I'm glad to hear you're feeling happy! Let's keep the good vibes going!";
}

function sadMoodResponse() {
  return "I'm sorry you're feeling sad. It's okay, take your time to talk about it.";
}

function angryMoodResponse() {
  return "I sense some anger. Would you like to talk about what's bothering you?";
}

function bullyingMoodResponse() {
  return "No one deserves to be bullied. You are strong, and I’m here to listen.";
}

function suicidalMoodResponse() {
  return "I'm really sorry you're feeling this way, but I can't provide the help you need. Please reach out to someone who can.";
}

function depressedMoodResponse() {
  return "It's tough to feel depressed, but you're not alone. Let’s talk about it.";
}

function provocativeMoodResponse() {
  return "Hey, I get it. Sometimes we need to vent, but let’s try to keep things respectful.";
}

function roastingMoodResponse() {
  return "Haha, I see you like a good roast! But don’t worry, I’ve got some funny comebacks for you.";
}

function userLeavingResponse() {
  return "Goodbye! Take care, and we can chat again whenever you need.";
}

function generalMoodResponse() {
  return "I’m here to chat whenever you need me!";
}

// POST endpoint to handle messages
app.post('/api/message', (req, res) => {
  const { message } = req.body;
  let moodDetected = "General";
  let responseMessage = generalMoodResponse(); // Default response

  // Check for trigger words and set the mood
  if (happyList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Happy";
    responseMessage = happyMoodResponse();
  } else if (sadList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Sad";
    responseMessage = sadMoodResponse();
  } else if (angryList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Angry";
    responseMessage = angryMoodResponse();
  } else if (bullyingList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Bullying";
    responseMessage = bullyingMoodResponse();
  } else if (suicidalList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Suicidal";
    responseMessage = suicidalMoodResponse();
  } else if (depressedList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Depressed";
    responseMessage = depressedMoodResponse();
  } else if (provocativeList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Provocative";
    responseMessage = provocativeMoodResponse();
  } else if (roastingList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Roasting";
    responseMessage = roastingMoodResponse();
  } else if (leavingList.some(word => message.toLowerCase().includes(word))) {
    moodDetected = "Leaving";
    responseMessage = userLeavingResponse();
  }

  console.log(`[Detected Mood: ${moodDetected}]`);

  // Send back the response message
  res.json({ message: responseMessage });
});

// Start the server
app.listen(5000, () => {
  console.log('Server is running on port 5000');
});
