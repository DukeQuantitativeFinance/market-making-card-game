from flask import Flask, jsonify, request, session, Blueprint
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from dotenv import load_dotenv
import os
from uuid import uuid4

from models.User import User
from database import db
from routes.maker_taker_card_game_routes import maker_taker_card_game_routes

load_dotenv()
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Allow CORS for development
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print("data: ", data)
    
    # search for existing user
    try:
        user = User.objects.get(email=data['email'])
    except:
        user = None
    if user:
        return jsonify({'error': 'User with this email already exists'})
    
    # create new user object and save to database
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user_id = str(uuid4())
    new_user = User(user_id=user_id, email=data['email'], password=hashed_password)
    new_user.save()
    session['user_id'] = user_id
    return jsonify({'message': 'User created successfully', 'userId': user_id})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects.get(email=data['email'])
    if user and bcrypt.check_password_hash(user.password, data['password']):
        session['user_id'] = user.user_id
        return jsonify({'message': 'Login successful', 'userId': user.user_id})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    # Remove user_id from session to log out the user
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'})

app.register_blueprint(maker_taker_card_game_routes)

if __name__ == '__main__':
    app.run(debug=True)
