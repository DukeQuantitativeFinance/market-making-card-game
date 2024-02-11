import React, { useState } from 'react';

import CardList from './CardList';

const MarketMakingCardGameInterface = () => {
  const [cards, setCards] = useState([{"value": 12, "suit": "spades"}, {"value": 12, "suit": "spades"}]);
  const [buyPrice, setBuyPrice] = useState('');
  const [sellPrice, setSellPrice] = useState('');
  const [buyQuantity, setBuyQuantity] = useState('');
  const [sellQuantity, setSellQuantity] = useState('');

  const handleBuyPriceChange = (e) => {
    setBuyPrice(e.target.value);
  };

  const handleSellPriceChange = (e) => {
    setSellPrice(e.target.value);
  };

  const handleBuyQuantityChange = (e) => {
    setBuyQuantity(e.target.value);
  };

  const handleSellQuantityChange = (e) => {
    setSellQuantity(e.target.value);
  };

  // const submitMarket = () => {
  //   try {
  //       const request = {
            
  //       }
  //       const response = await axios.post(`${process.env.REACT_APP_BACKEND_URL}/market-making-card-game/submit-market`);
  //     } catch (error) {
  //       console.error('Error fetching open games:', error);
  //     }
  // };

  return (
    <div>
      <h1>Market Making Card Game Interface</h1>
      <div className="cards">
        <CardList
            cards={cards}
        />
      </div>
      <div className="inputs">
        <label>Buy Price:</label>
        <input type="number" id="buyPrice" value={buyPrice} onChange={handleBuyPriceChange} />
        <label>Buy Quantity:</label>
        <input type="number" id="buyQuantity" value={buyQuantity} onChange={handleBuyQuantityChange} />
        <label>Sell Price:</label>
        <input type="number" id="sellPrice" value={sellPrice} onChange={handleSellPriceChange} />
        <label>Sell Quantity:</label>
        <input type="number" id="sellQuantity" value={sellQuantity} onChange={handleSellQuantityChange} />
      </div>
      <div>
        <button>Submit Market</button>
      </div>
    </div>
  );
};

export default MarketMakingCardGameInterface;
