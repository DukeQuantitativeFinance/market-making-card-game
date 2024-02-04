import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';

import { UserContext } from '../UserContext';

const MarketMakingCardGameLobby = () => {
  const { userId, updateUser } = useContext(UserContext);
  const [games, setGames] = useState([]);

  const fetchOpenGames = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/market-making-card-game/open-games`);
      setGames(response.data.game_list); // Assuming the response contains an array of open games
    } catch (error) {
      console.error('Error fetching open games:', error);
    }
  };

  const createGame = async () => {
    try {
      const request = {"user_id": userId, "lobby_name": `Lobby ${userId}`};
      await axios.post(`${process.env.REACT_APP_BACKEND_URL}/market-making-card-game/create-game`, request)
      .then(response => {
        console.log('Response:', response.data);
      })
      .catch(error => {
        console.error('Error:', error.response.data);
      });
    } catch (error) {
      console.error('Error fetching open games:', error);
    }
  }

  const joinGame = (gameId) => {
    console.log('Joining game:', gameId);
  };

  useEffect(() => {
    // Fetch open games initially
    fetchOpenGames();

    // Poll server every 3 seconds for updates
    const interval = setInterval(fetchOpenGames, 3000);

    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return (
    <div className="lobby-container">
      <h2>Market Making Card Game</h2>
      <div>
        <button onClick={createGame}>Create game</button>
      </div>
      <div className="games-list">
        {games.map((game, index) => (
          <div key={index} className="game">
            <h3>{game.name}</h3>
            <p>Remaining slots: {game.remainingSlots}</p>
            {/* Add button to join the game */}
            <button onClick={() => joinGame(game.id)}>Join Game</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MarketMakingCardGameLobby;
