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
    return render_template('form.html', query = ())

@app.route('/save', methods=['POST'])
def post():
    new_post = {}
    new_post['title'] = request.form['title']
    new_post['story'] = request.form['story']
    new_post['criteria'] = request.form['criteria']
    new_post['value'] = request.form['value']
    new_post['time'] = request.form['time']
    new_post['status'] = request.form['status']
    print (request.form['id'])
    # if request.form['id'] != None:
    #     id_to_delete = request.form['id']
    #     UserStory.delete_user_story(int(id_to_delete[0]))

    UserStory.add_user_story(new_post)

    return redirect('/list')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def send():
    query_to_print = UserStory.list_all()
    return render_template('list.html', query=query_to_print)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    to_edit = request.form['default']
    id = int(to_edit[0])
    query_to_edit = UserStory.list_to_edit(id)
    return render_template('form.html', query = query_to_edit)




# db.create_tables([UserStory])
app.run()