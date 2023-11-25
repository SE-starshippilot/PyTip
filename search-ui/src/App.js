// import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';
var data = require('./mock_data.json');

function App() {
  const [value, setValue] = useState('');

  const onChange = (event) => {
    setValue(event.target.value);
  }

  const onSearch = (searchTerm) => {
    console.log(searchTerm)
    //API
  }

  useEffect(() => {
    const interval = setInterval(() => {
      // Send value to port 8080
      fetch('http://localhost:8080', {
        method: 'POST',
        body: JSON.stringify({ value }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        // Handle response from server
        console.log(data);
      })
      .catch(error => {
        // Handle error
        console.error(error);
      });
    }, 2000);

    return () => {
      clearInterval(interval);
    };
  }, [value]);

  return (
    <div className="App">
      <h1>PyHint</h1>
      <div className='search-container'>
        <div className='search-box'>
          <input type='text' placeholder='Search' value={value} onChange={onChange}/>
          <button onClick={()=>onSearch(value)}>Search</button>
          {/* <div className='Dropdown'>
            {
              data.filter(
                item => {
                  const searchItem = value.toLowerCase();
                  const fullName = item.full_name.toLowerCase();
                  return searchItem && fullName.startsWith(searchItem);
                }
              ).
              map((item) => {
                return (
                  <div className='Dropdown-item'>
                    <div className='Dropdown-item-title'>
                      {item.full_name}
                    </div>
                  </div>
                )
              })
            }
          </div> */}
        </div>
      </div>
    </div>
  );
}

export default App;
