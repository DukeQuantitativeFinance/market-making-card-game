import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const AuthPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // Perform login logic here
    const request = {
      "email": email,
      "password": password,
    }
    axios.post(`${process.env.REACT_APP_BACKEND_URL}/login`, request)
    .then(response => {
      console.log('Response:', response.data);
      // Handle successful response
      console.log("navigate to lobby");
      navigate('/lobby');
    })
    .catch(error => {
      console.error('Error:', error.response.data);
      // Handle error response
    });
  };

  const handleRegister = (e) => {
    e.preventDefault();
    // Perform login logic here
    const request = {
      "email": email,
      "password": password,
    }
    axios.post(`${process.env.REACT_APP_BACKEND_URL}/signup`, request)
    .then(response => {
      console.log('Response:', response.data);
      // Handle successful response
    })
    .catch(error => {
      console.error('Error:', error.response.data);
      // Handle error response
    });
  };

  return (
    <div className="login-container">
      <h2>Login/Register to DQF Trading Games</h2>
      <form>
        <div className="form-group">
          <label>Email:</label>
          <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button onClick={handleRegister}>Register</button>
        <button onClick={handleLogin}>Login</button>
      </form>
    </div>
  );
};

export default AuthPage;
