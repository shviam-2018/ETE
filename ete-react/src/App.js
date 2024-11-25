import React, { useState } from 'react';

function App() {
  // State to hold the user input and the response from Flask
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  // Handle input changes
  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch('http://localhost:5000/api/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input: input }),
    });
    
    const data = await res.json();
    setResponse(data.message); // Set the response from Flask
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>ETE React App</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            value={input}
            onChange={handleInputChange}
            placeholder="Enter your message"
            style={{ padding: '10px', fontSize: '16px', width: '300px', marginRight: '10px' }}
          />
          <button type="submit" style={{ padding: '10px 20px', fontSize: '16px' }}>
            Submit
          </button>
        </div>
      </form>

      {/* Display the response from Flask */}
      {response && (
        <div
          style={{
            marginTop: '20px',
            padding: '20px',
            border: '1px solid #ccc',
            borderRadius: '8px',
            backgroundColor: '#f9f9f9',
            maxWidth: '400px',
            wordWrap: 'break-word',
          }}
        >
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
