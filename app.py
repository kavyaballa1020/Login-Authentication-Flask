from flask import Flask, render_template, request, redirect, session
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

if mongo.db is not None:
    print("MongoDB connected successfully!")
else:
    print("MongoDB connection failed!")


@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = mongo.db.register
        user_data = users.find_one({'username': username})

        if user_data and bcrypt.check_password_hash(user_data['password'], password):
            session['username'] = username
            
            login_sessions = mongo.db.login_sessions
            login_sessions.insert_one({'username': username})
            
            return redirect('/secured')
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']

        users = mongo.db.register
        existing_user = users.find_one({'username': username})

        if existing_user:
            return "Username already exists. <a href='/register'>Try again</a>"

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users.insert_one({'first_name': first_name, 'last_name': last_name, 'username': username, 'password': hashed_password})
        return redirect('/login')
    return render_template('register.html')


@app.route('/secured')
def secured():
    if 'username' in session:
        users = mongo.db.register
        user_data = users.find_one({'username': session['username']})

        first_name = user_data.get('first_name', '')
        last_name = user_data.get('last_name', '')

        return render_template('secured_page.html', first_name=first_name, last_name=last_name)
    else:
        return redirect('/login')
    
    
@app.route('/logout')
def logout():
    if 'username' in session:
        login_sessions = mongo.db.login_sessions
        login_sessions.delete_one({'username': session['username']})

    session.pop('username', None)

    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
