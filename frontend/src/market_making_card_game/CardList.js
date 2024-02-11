import React, { useState, useEffect, useContext } from 'react';
import { PlayingCard } from "@alehuo/react-playing-cards";

const CardList = ({ cards }) => {  
    console.log("cards: ", cards);
    return (
      <div>
        {cards.map((card, index) => (
          <PlayingCard key={index} value={card.value} suit={card.suit} />
        ))}
      </div>
    );
  };
  
  export default CardList;