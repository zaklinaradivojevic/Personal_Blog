from main import app, db, User

@app.shell_context_processor
def make_shell_context():
 return dict(app=app, db=db, User=User)

#$ export FLASK_APP=manage.py
# $ flask shell
# >>> db.create_all()