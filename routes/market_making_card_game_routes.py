from flask import Flask, jsonify, request, Blueprint, render_template, session
from uuid import uuid4

from models.Game import Game

market_making_card_game_routes = Blueprint('market_making_card_game_routes', __name__)
active_games = []

@market_making_card_game_routes.route('/market-making-card-game/lobby')
def lobby():
    games = Game.objects()  # Retrieve all games from the database
    return render_template('market_making_card_game_lobby.html', games=games)

@market_making_card_game_routes.route('/market-making-card-game/active-games', methods=['POST'])
def get_active_games():
    games_data = []
    for game in active_games:
        game_data = {
            'game_id': str(game.game_id),  # Convert UUID to string if necessary
            'name': game.name,
            'created_by': game.created_by,
        }
        games_data.append(game_data)
    return jsonify(games_data)

@market_making_card_game_routes.route('/market-making-card-game/join_game', methods=['POST'])
def join_game():
    game_id = request.form.get('game_id')
    # Add logic to join the game (e.g., update database)
    # Example:
    # game = Game.objects.get(game_id=game_id)
    # game.players.append(current_user)
    # game.save()
    return jsonify({'success': True})

@market_making_card_game_routes.route('/market-making-card-game/create-game', methods=['POST'])
def create_game():
    # parse request data
    data = request.json
    name = data.get('name')
    created_by = session.get('username')
    
    # generate unique game ID
    game_id = str(uuid4())

    # create a new game object
    new_game = Game(
        game_id=game_id,
        name=name,
        created_by=created_by
    )

    # add the new game to the list of active games
    active_games.append(new_game)

    return jsonify({'success': True, 'game_id': game_id})