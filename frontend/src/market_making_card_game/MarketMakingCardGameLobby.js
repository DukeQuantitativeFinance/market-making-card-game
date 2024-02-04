import React, { useState, useEffect } from 'react';
import axios from 'axios';

const MarketMakingCardGameLobby = () => {
  const [games, setGames] = useState([]);

  const fetchOpenGames = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/market-making-card-game/open-games`);
      setGames(response.data); // Assuming the response contains an array of open games
    } catch (error) {
      console.error('Error fetching open games:', error);
    }
  };

  const joinGame = (gameId) => {
    console.log('Joining game:', gameId);
  };

  useEffect(() => {
    // Fetch open games initially
    fetchOpenGames();

    // Poll server every 10 seconds for updates
    const interval = setInterval(fetchOpenGames, 10000);

    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, []); // Empty dependency array ensures the effect runs only once on mount

  return (
    <div className="lobby-container">
      <h2>Market Making Card Game</h2>
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
