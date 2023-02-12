import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import axios from 'axios';
import './App.css';



const MyComponent = () => {
    const [response, setResponse] = useState(null);
  
    const handleClick = async () => {
      const res = await fetch('http://localhost:5000/route');
      const data = await res.text();
      setResponse(data);
    };
  
    return (
      <div>
        <button type="button" onClick={handleClick}>
          Generate Patient Statistics
        </button>
        {response && (
          <p>Dear patient, your personal includes the clinical status of  {response}</p>
        )}
      </div>
    );
  };


export default MyComponent;