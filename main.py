from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
import datetime
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "abc"
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
class User(db.Model):
     __tablename__ = 'user_table_name'

     id = db.Column(db.Integer, primary_key=True)
     email = db.Column(db.String(255), unique=True, nullable=False)
     username = db.Column(db.String(255), nullable=False, index=True,unique=True)
     password = db.Column(db.String(255), nullable=False)
     posts = db.relationship('Post', backref='user',lazy='dynamic')
      
def __init__(self, username):
 self.username = username
 
def __repr__(self):
     return "<User '{}'>".format(self.username)


tags = db.Table('post_tags',
 db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
 db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)
class Post(db.Model):
 id = db.Column(db.Integer(), primary_key=True)
 title = db.Column(db.String(255), nullable=False)
 text = db.Column(db.Text())
 publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)
 comments = db.relationship('Comment',backref='post',lazy='dynamic')
 user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
 tags = db.relationship('Tag',secondary=tags,backref=db.backref('posts', lazy='dynamic'))
 
def __init__(self, title):
 self.title = title
 
def __repr__(self):
 return "<Post '{}'>".format(self.title)

class Tag(db.Model):
 id = db.Column(db.Integer(), primary_key=True)
 title = db.Column(db.String(255), nullable=True, unique=True)
 
def __init__(self, title):
 self.title = title
 
def __repr__(self):
 return "<Tag '{}'>".format(self.title)

class Comment(db.Model):
 id = db.Column(db.Integer(), primary_key=True)
 name = db.Column(db.String(255), nullable=False)
 text = db.Column(db.Text())
 date = db.Column(db.DateTime(), default=datetime.datetime.now)
 post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
 
def __repr__(self):
 return "<Comment '{}'>".format(self.text[:15])


@app.route('/')
def home():    
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
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

@app.route('/table')
def table(): 
    result = "<h1>Tables</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1320)
