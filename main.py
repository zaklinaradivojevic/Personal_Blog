from flask import Flask, render_template, request, flash, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "abc"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.init_app(app)
    db.create_all()
 

@app.route('/')
def home():    
    return render_template("home.html")

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
    return render_template('login.html')

   


@app.route('/register', methods=['GET', 'POST'])
def register():
     return render_template('sign_in.html')


@app.route('/logout')
def logout():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1320)
