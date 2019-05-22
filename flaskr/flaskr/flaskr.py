#all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash


app = Flask(__name__) #create the application instance
app.config.from_object(__name__) # load config from this file, flaskr.py

#Load default config and override config from an environment variable
#app.config에 dictionary 형식으로 인자들을 저장 : 환경변수들
app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'), #absolute path merging
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    """Connects to the specific database"""
    rv = sqlite3.connect(app.config['DATABASE']) # 위의 저장한 DB랑 연결!
    #connect 만들어 주고
    rv.row_factory = sqlite3.Row
    #
    return rv
    #이제 이 rv에다 대고(connect_db()) 커서를 만들어 쓸거임

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    '''db 닫기'''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schemal.sql',mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    '''initalize the database'''
    init_db()
    print('Initialized the db')

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html',entries=entries)

@app.route('add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                [request.form['title'],request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.methods == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login_html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))