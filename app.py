from flask import Flask, render_template, request, redirect, session, url_for
from mongoengine import connect

from models.User import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# configure MongoEngine
connect(
    db='your_database_name',
    host='mongodb://localhost/your_database_name',
    alias='default'
)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

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

if __name__ == '__main__':
    app.run(debug=True)
