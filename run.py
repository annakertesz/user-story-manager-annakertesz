from flask import *
import sqlite3
from models import *


app = Flask('school_system')
app.config['DEBUG'] = True

# DB connector
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/story')
def apply():
    return render_template('form.html')

@app.route('/save', methods=['POST'])
def post():
    new_post = {}
    new_post['title'] = request.form['title']
    new_post['story'] = request.form['story']
    new_post['criteria'] = request.form['criteria']
    new_post['value'] = request.form['value']
    new_post['time'] = request.form['time']
    new_post['status'] = request.form['status']
    UserStory.add_user_story(new_post)
    return redirect('/list')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def send():
    query_to_print = UserStory.list_all()
    return render_template('list.html', query=query_to_print)

# db.create_tables([UserStory])
app.run()