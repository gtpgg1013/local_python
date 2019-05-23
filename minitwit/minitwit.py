from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
import time
#closing method는 with 구문과 함께 사용
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash


#configuration
DATABASE = 'minitwit.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

#환경설정
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS',silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    # with closing(connect_db()) as db:
    with app.open_resource('schema.sql', mode='r') as f:
        connect_db().cursor().executescript(f.read())
    connect_db().commit()
    connect_db().close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query,args)
    rv = [dict((cur.description[idx][0], value)
            for idx, value in enumerate(row)) for row in cur.fetchall()]
    #cur.fetchall()에 있는 애들을 1줄씩 꺼내서 
    #그 한줄씩 꺼낸 애들을 index와 value로 나눈 다음
    #description과 밸류로 나눠서 딕셔너리화 한 걸 rv 리스트에 때려넣은것
    return (rv[0] if rv else None) if one else rv

def get_user_id(username):
    rv = g.db.execute('select user_id from user where username = ?',
                        [username]).fetchone()
    return rv[0] if rv else None

def format_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')

def gravatar_url(email, size=80):
    return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
        (md5(email.strip().lower().encode('utf-8')).hexdigest(), size)

@app.before_request
def before_request():
    '''
    세션 만들기
    '''
    g.db = connect_db()
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = ?',
                            [session['user_id']],one=True)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g,'db'):
        g.db.close()

@app.route('/')
def timeline():
    if not g.user:
        return redirect(url_for('public_timeline'))
    return render_template('timeline.html', messages=query_db('''
        select message.*, user.* from message, user
        where message.author_id = user.user_id and (
            user.user_id = ? or
            user.user_id in (select whom_id from follower
                                where who_id = ?))
        order by message.pub_date desc limit?''',
        [session['user_id'], session['user_id'], PER_PAGE]))

@app.route('/public')
def public_timeline():
    return render_template('timeline.html', messages=query_db('''
        select message.*, user.* from message, user
        where message.author_id = user.user_id
        order by message.pub_date desc limit ?''', [PER_PAGE]))

@app.route('/<username>')
def user_timeline(username):
    profile_user = query_db('select * from user where username = ?',
                            [username], one=True)
    if profile_user is None:
        abort(404)
    followed = False
    if g.user:
        followed = query_db('''select 1 from follwer where
            follower.who_id = ? and follower.whom_id = ?''',
            [session['user_id'], profile_user['user_id']],
            one=True) is not None
    return render_template('timeline_html',messages=query_db('''
            select message.*, user.* from message, user where
            user.user_id = message.author_id and user.user_id = ?
            order by message.pub_date desc limt ?''',
            [profile_user['user_id'],PER_PAGE]), followed=followed,
            profile_user=profile_user)

@app.route('/<username>/follow')
def follow_user(username):
    '''현재 유저를 주어진 유저의 follower로 만들기'''
    if not g.user:
        abort(401)
    whom_id = get_user_id(username)
    g.db.execute('insert into follower (who_id, whom_id) values (?,?)',
                [session['user_id'], whom_id])
    g.db.commit()
    flash('You are now following "%s"' %username)
    return redirect(url_for('user_timeline', username=username))

@app.route('/<username>/unfollow')
def unfollow_user(username):
    '''현재 유저를 주어진 유저를 unfollow하게 하기'''
    if not g.user:
        abort(401)
    whom_id = get_user_id(username)
    if whom_id is None:
        abort(404)
    g.db.execute('delete from follower where who_id = ? and whom_id = ?',
                    [session['user_id'], whom_id])
    g.db.commit()
    flash('You are no longer following "%s"' % username)
    return redirect(url_for('user_timeline', username=username))

@app.route('/add_message', methods=['POST'])
def add_message():
    '''새 메시지를 등록'''
    if 'user_id' not in session:
        abort(401)
    if request.form['text']:
        g.db.execute('''insert into
            message (author_id, text, pub_date)
            values (?, ?, ?)''', (session['user_id'], request.form['text'], int(time.time())))

@app.route('/login', methods=['GET','POST'])
def login():
    '''로그인'''
    if g.user:
        return redirect(url_for('timeline'))
    error=None
    if request.method == 'POST':
        user = query_db('''select * from user where
            username = ?''', [request.form['username']], one=True)
            #여기서 one이면 rv[0] : 맨위에꺼 말하는건가?
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['pw_hash'],
                                        request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['user_id']
            return redirect(url_for('timeline'))
    return render_template('login_html',error=error)

@app.route('/register',methods=['GET','POST'])
def register():
    '''회원가입'''
    if g.user:
        return redirect(url_for('timeline'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or \
            '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = "The two passwords do not match"
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            g.db.execute('''insert into user (
                username, email, pw_hash) values (?,?,?)''',
                [request.form['username'],request.form['email'],
                generate_password_hash(request.form['password'])])
            g.db.commit()
            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
        return render_template('register.html',error=error)

@app.route('/logout')
def logout():
    '''로그아웃'''
    flash('You were logged out')
    session.pop('user_id', None)
    return redirect(url_for('public_timeline'))

#add some filters to jinja
# app.jinja_env.filters['datetimeformat'] = format_datetime
# app.jinja_env.filters['gravatar'] = gravatar_url

if __name__ == '__main__':
    init_db()
    app.run()