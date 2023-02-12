import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import axios from 'axios';
import './App.css';

const MyComponent = () => {
    const [fileNames, setFileNames] = useState([]);

    useEffect(() => {
        axios.get('/api/files')
          .then((response) => {
            setFileNames(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      }, []);

    const handleButtonClick = () => {

    };

    return (
      <div>
        <button onClick={handleButtonClick}>Click me</button>
        <ul>
          {fileNames.map((fileName, index) => (
            <li key={index}>{fileName}</li>
          ))}
        </ul>
      </div>
    );
};


export default MyComponent;