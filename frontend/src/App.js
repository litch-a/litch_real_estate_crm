import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/properties/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => console.error('API error:', err));
  }, []);

  return (
    <div className="App">
      <h1>Essential CRM</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}

export default App;