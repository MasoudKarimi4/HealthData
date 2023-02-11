import React from 'react';
import logo from './logo.svg';
import './App.css';

class MyComponent extends React.Component {
    handleButtonClick = () => {
     // const child = spawn('./path/to/your/script.sh');
  
  //child.stdout.on('data', data => {
    //    console.log(`Child output: ${data}`);
    //  });
  
    //  child.stderr.on('data', data => {
     //   console.error(`Child error: ${data}`);
    //  });
    };
  
    render() {
      return (
        <div>
          <button onClick={this.handleButtonClick}>Retrieve Random JSON</button>
        </div>
      );
    }
  }

export default MyComponent;