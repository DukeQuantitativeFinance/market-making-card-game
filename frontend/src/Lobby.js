import React from 'react';
import { Link } from 'react-router-dom';

const Lobby = () => {
  return (
    <div>
      <h1>Lobby</h1>
      <ul>
        <li><Link to="/market-making-card-game/">Market Making Card Game</Link></li>
      </ul>
    </div>
  );
};

export default Lobby;
