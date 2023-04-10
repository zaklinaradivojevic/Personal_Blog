from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask import Flask, render_template, request, flash, redirect, url_for

from werkzeug.security import check_password_hash
from models import db, User

import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

# Initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
# import login_manager from models.py and initialize it with app
from models import login_manager

login_manager.init_app(app)

# Define the function to load a user from the user ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id=post_id)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Add new post to database
        return 'Post added!'
    else:
        return render_template('new_post.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Get user from the database by username
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            # Log the user in and redirect to the home page
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('home'))

        # If the user doesn't exist or the password is incorrect, show an error message
        flash('Invalid username or password.', 'error')

    # Render the login form
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
