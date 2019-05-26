from __future__ import with_statement
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash

#일단 넘버로 하고 유저이름을 치면 redirect하는걸로..?

#configration
DATABASE = 'tripex.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('TRIPEX_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
            for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def get_user_num(userID):
    rv = g.db.execute('select userNum from user where userID = ?',
                        [userID]).fetchone()
    return rv[0] if rv else None

def format_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')

def gravatar_url(email, size=80):
    return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
        (md5(email.strip().lower().encode('utf-8')).hexdigest(), size)

@app.before_request
def before_request():
    g.db = connect_db()
    g.user = None
    if 'userNum' in session:
        g.user = query_db('select * from user where userNum = ?',
                            [session['userNum']], one=True)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g,'db'):
        g.db.close()

@app.route('/')
def timeline():
    if not g.user:
        return redirect(url_for('public_timeline'))
    return render_template('timeline.html', postings=query_db('''
        select posting.*, user.* from posting, user
        where posting.userNum = user.userNum and (
            user.userNum = ? or
            user.userNum in (select whom_num from follower
                                where who_num = ?))
        order by posting.pubTime desc limit ?''',
        [session['userNum'], session['userNum'], PER_PAGE]))

@app.route('/public')
def public_timeline():
    return render_template('timeline.html', postings=query_db('''
        select posting.*, user.* from posting, user
        where posting.userNum = user.userNum
        order by posting.pubTime desc limit ?''', [PER_PAGE]))

@app.route('/<userID>')
def user_timeline(userID):
    profile_user = query_db('select * from user where userID = ?',
                            [userID], one=True)
    if profile_user is None:
        abort(404)
    followed = False
    if g.user:
        followed = query_db('''select 1 from follower where
            follower.who_num = ? and follower.whom_num = ?''',
            [session['userNum'], profile_user['userNum']],
            one=True) is not None
    return render_template('timeline.html',postings=query_db('''
            select posting.*, user.* from posting, user where
            user.userNum = posting.userNum and user.userNum = ?
            order by posting.pubTime desc limit ?''',
            [profile_user['userNum'], PER_PAGE]), followed=followed,
            profile_user=profile_user)

@app.route('/<userID>/follow')
def follow_user(userID):
    if not g.user:
        abort(401)
    whom_num = get_user_num(userID)
    if whom_num is None:
        abort(404)
    g.db.execute('insert into follower (who_num, whom_num) values (?, ?)',
                    [session['userNum'], whom_num])
    g.db.commit()
    flash('You are now following "%s"' % userID )
    return redirect(url_for('user_timeline',userID=userID))

@app.route('/<userID>/unfollow')
def unfollow_user(userID):
    if not g.user:
        abort(401)
    whom_num = get_user_num(userID)
    if whom_num is None:
        abort(401)
    g.db.execute('delete from follower where who_num=? and whom_num=?',
                    [session['userNum'],whom_num])
    g.db.commit()
    flash('You are no longer following "%s"' % userID)
    return redirect(url_for('user_timeline',userID=userID))

#title, destination1,2가 추가됨
@app.route('/add_posting', methods=['POST'])
def add_posting():
    if 'userNum' not in session:
        abort(401)
    if request.form['title']:
        if request.form['contents']:
            g.db.execute('''insert into
                posting (userNum, title, contents, pubTime)
                values (?, ?, ?, ?)''',(session['userNum'],
                request.form['title'], request.form['contents'],int(time.time())))
            g.db.commit()
            flash('Your posting was recorded')
    else:
        flash('내용을 입력해 주세요')
    return redirect(url_for('timeline'))

@app.route('/register', methods=['GET','POST'])
def register():
    if g.user:
        return redirect(url_for('timeline'))
    error=None
    if request.method == 'POST':
        if not request.form['name']:
            error='You have to enter a name'
        elif not request.form['email'] or '@' not in request.form['email']:
            error='You have to enter a vaild email address'
        elif not request.form['address']:
            error='You have to enter your address'
        elif not request.form['interestedPlace1']:
            error='You have to enter your interestedPlace'
        elif not request.form['interestedPlace2']:
            error='You have to enter your interestedPlace'
        elif not request.form['userID']:
            error='You have to enter your ID'
        elif not request.form['password']:
            error='You have to enter your password'
        elif not request.form['interest']:
            error='You have to enter your interest'
        elif not request.form['tripstyle']:
            error='You have to enter your tripstyle'
        elif get_user_num(request.form['userID']) is not None:
            error='This ID is already taken'
        else:
            g.db.execute('''insert into user (
                name, email, address, interestedPlace1, interestedPlace2,
                userID, password, interest, tripstyle, pubTime)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                [request.form['name'], request.form['email'], request.form['address'],
                request.form['interestedPlace1'], request.form['interestedPlace2'],
                request.form['userID'], generate_password_hash(request.form['password']),
                request.form['interest'], request.form['tripstyle'], int(time.time())])
            g.db.commit()
            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('register.html',error=error)

@app.route('/login', methods=['GET','POST'])
def login():
    if g.user:
        return redirect(url_for('timeline'))
    error=None
    if request.method == 'POST':
        user = query_db('''select * from user where
            userID = ?''', [request.form['userID']], one=True)
        if user is None:
            error = 'Invalid userID'
        elif not check_password_hash(user['password'], \
                                        request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['userNum'] = user['userNum']
            return redirect(url_for('timeline'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    flash('You were logged out')
    session.pop('userNum', None)
    return redirect(url_for('public_timeline'))

app.jinja_env.filters['datetimeformat'] = format_datetime
app.jinja_env.filters['gravatar'] = gravatar_url

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80, debug=True)