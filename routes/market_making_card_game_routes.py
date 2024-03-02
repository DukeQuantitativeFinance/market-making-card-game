from flask import Flask, jsonify, request, Blueprint, render_template, session, redirect
from uuid import uuid4

from models.Game import Game

market_making_card_game_routes = Blueprint('market_making_card_game_routes', __name__)
active_games = {} # map of game id to game object

@market_making_card_game_routes.route('/market-making-card-game/lobby')
def lobby():
    return render_template('market_making_card_game_lobby.html')

@market_making_card_game_routes.route('/market-making-card-game/active-games', methods=['POST'])
def get_active_games():
    games_data = []
    # iterate over all active games and return their info
    for game_id in active_games:
        game = active_games[game_id]
        game_data = {
            'game_id': str(game.game_id),
            'name': game.name,
            'created_by': game.created_by,
            'player_count': len(game.players)
        }
        games_data.append(game_data)
    return jsonify(games_data)

@market_making_card_game_routes.route('/market-making-card-game/join-game', methods=['POST'])
def join_game():
    try:
        # parse request
        data = request.json
        username = session.get('username')
        game_id = data.get('game_id')
        
        # add player to game
        if game_id in active_games:
            game = active_games[game_id]
            if username not in game.players:
                game.players.append(username)
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

@market_making_card_game_routes.route('/market-making-card-game/create-game', methods=['POST'])
def create_game():
    try:
        # parse request data
        data = request.json
        name = data.get('name')
        created_by = session.get('username')
        
        # generate unique game ID
        game_id = str(uuid4())

        players = [created_by]

        # create a new game object
        new_game = Game(
            game_id=game_id,
            name=name,
            created_by=created_by,
            players=players
        )

        # add the new game to the list of active games
        active_games[game_id] = new_game

        return jsonify({'success': True, 'game_id': game_id})
    except:
        return jsonify({'success': False}) 

@market_making_card_game_routes.route('/market-making-card-game/game/<game_id>')
def game_interface(game_id):
    # Retrieve game details and list of players from the database
    game = active_games[game_id]
    players = game.players
    
    is_creator = False
    if 'username' in session and session['username'] == game.created_by:
        is_creator = True

    return render_template('market_making_card_game_interface.html', game=game, players=players, is_creator=is_creator)

@market_making_card_game_routes.route('/leave_game', methods=['POST'])
def leave_game():
    game_id = request.form.get('game_id')
    # Add logic to remove the current user from the game (e.g., update database)
    # Example:
    # game = Game.objects.get(game_id=game_id)
    # game.players.remove(current_user)
    # game.save()
    return redirect('/market-making-card-game/lobby')  # Redirect to lobby page after leaving game