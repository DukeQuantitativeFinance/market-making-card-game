from flask import Flask, jsonify, request, Blueprint
from uuid import uuid4

from models.Game import Game

maker_taker_card_game_routes = Blueprint('maker_taker_card_game_routes', __name__)
games = {}

@maker_taker_card_game_routes.route('/maker_taker_card_game/create-game', methods=['POST'])
def create_game():
    data = request.json
    game_name = data.get('lobby_name')
    game_host = data.get('user_id')
    game_id = uuid4()
    games[game_id] = Game(game_id=game_id, name=game_name, users=[], status="open", game_host=game_host)
    
    return jsonify({'game_id': game_id, 'game_name': game_name}), 201

@maker_taker_card_game_routes.route('/maker_taker_card_game/open-games', methods=['GET'])
def open_games():
    game_list = []
    for game in games:
        game_list.append(game)
    return jsonify({'game_list': game_list}), 201