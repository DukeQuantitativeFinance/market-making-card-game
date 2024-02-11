import React, { useState, useEffect } from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';

import './App.css';

import AuthPage from './auth/Auth';
import MarketMakingCardGameLobby from './market_making_card_game/MarketMakingCardGameLobby';
import Lobby from './Lobby';
import { UserProvider } from './UserContext';
import MarketMakingCardGameInterface from './market_making_card_game/MarketMakingCardGameInterface';

function App() {
  return (
    <UserProvider>
      <div className="App">
        <Routes>
          {/* GENERAL LOGIN */}
          <Route
            exact
            path={'/auth'}
            element={<AuthPage/>}
          />

          {/* GENERAL LOBBY */}
          <Route
            exact
            path={'/lobby'}
            element={<Lobby/>}
          />

          {/* MARKET MAKING CARD GAME HOME PAGE */}
          <Route
            exact
            path={'/market-making-card-game/'}
            element={<MarketMakingCardGameLobby />}
          />

          {/* MARKET MAKING CARD GAME INTERFACE */}
          <Route
            exact
            path={'/market-making-card-game/play'}
            element={<MarketMakingCardGameInterface />}
          />
        </Routes>
      </div>
    </UserProvider>
  );
}

export default App;
