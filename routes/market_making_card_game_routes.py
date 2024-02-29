from flask import Flask, jsonify, request, Blueprint, render_template
from uuid import uuid4

from models.Game import Game

market_making_card_game_routes = Blueprint('market_making_card_game_routes', __name__)

@market_making_card_game_routes.route('/market-making-card-game/lobby')
def lobby():
    games = Game.objects()  # Retrieve all games from the database
    return render_template('market_making_card_game_lobby.html', games=games)

@market_making_card_game_routes.route('/market-making-card-game/join_game', methods=['POST'])
def join_game():
    game_id = request.form.get('game_id')
    # Add logic to join the game (e.g., update database)
    # Example:
    # game = Game.objects.get(game_id=game_id)
    # game.players.append(current_user)
    # game.save()
    return jsonify({'success': True})