import React from 'react';
import logo from './logo.svg';
import './App.css';
import MyComponent from './button.js'

function App() {
  return (

    <div className="App">
      <header className="App-header">
        
        <h1>MedData</h1>
        
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <MyComponent />
      </header>
    </div>
  );
}

export default App;
