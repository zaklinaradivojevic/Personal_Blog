from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

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
      
#pip install google-api-python-client
#pip install --upgrade pip
#pip install google-auth==2.0.2 google-auth-oauthlib==0.4.6 google-auth-httplib2==0.1.0 google-api-python-client==2.15.0
#pip install --no-cache-dir google-auth
#pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org google-auth==2.0.2

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        user = c.fetchone()

        if user is not None and check_password_hash(user[2], password):
            session['username'] = username
            conn.close()
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password.'
            conn.close()
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/search')
def search():
    # Your code here
    return render_template('search.html')




app.run(debug=True, host='0.0.0.0', port=8080)
#flask run --debugger --reload --host=0.0.0.0
