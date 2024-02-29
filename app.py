from flask import Flask, render_template, request, redirect, session, url_for
from mongoengine import connect
from dotenv import load_dotenv
import os
from uuid import uuid4

from models.User import User
from routes.market_making_card_game_routes import market_making_card_game_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# configure MongoEngine
load_dotenv()
DB_URI = os.getenv('MONGODB_URI')
db = connect("MarketMakingCardGame",
             host=DB_URI,
             alias='default')

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username already exists
        if User.objects(username=username).first():
            return render_template('signup.html', message='Username already exists')
        # Create new user
        user_id = str(uuid4())  # Generate unique user_id
        user = User(user_id=user_id, username=username, password=password)
        user.save()
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.objects(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def homepage():
    return render_template('home.html', username=session.get('username'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

app.register_blueprint(market_making_card_game_routes)

if __name__ == '__main__':
    app.run(debug=True)
