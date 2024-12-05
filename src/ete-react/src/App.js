import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Ensure you have appropriate styles for chat UI

function App() {
  const [userMessage, setUserMessage] = useState('');
  const [messages, setMessages] = useState([]); // To store the chat history
  const messagesEndRef = useRef(null); // For auto-scrolling to the bottom

  const handleSendMessage = async () => {
    if (!userMessage) return;

    // Add the user's message to the chat history
    const newMessages = [...messages, { text: userMessage, sender: 'user' }];
    setMessages(newMessages);
    setUserMessage('');

    try {
      // Send the user message to the backend and get the response
      const response = await axios.post('http://localhost:5000/api/message', { message: userMessage });
      const aiMessage = response.data.message;

      // Add the AI's response to the chat history
      setMessages([...newMessages, { text: aiMessage, sender: 'ai' }]);
    } catch (error) {
      console.error('Error fetching AI response:', error);
    }
  };

  // Scroll to the bottom of the chat when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="App">
      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === 'user' ? 'user-message' : 'ai-message'}`}
            >
              {msg.text}
            </div>
          ))}
          <div ref={messagesEndRef} /> {/* To scroll to the bottom */}
        </div>
      </div>
      <div className="input-container">
        <input
          type="text"
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          placeholder="Type a message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
