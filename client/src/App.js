import React from 'react';
import logo from './logo.svg';
import './App.css';
import MyComponent from './button.js'


function App() {
  return (

    <div className="App">
      <header className="App-header">
        
        <h1>MedData</h1>
        
        <p>
            Get relevant insight into your patient data.
        </p>
     
        <MyComponent />
      </header>
    </div>
  );
}

export default App;
