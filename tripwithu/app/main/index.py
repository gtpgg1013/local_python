from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from app.module import dbModule

main = Blueprint('main',__name__,url_prefix='/')

@main.route('/',methods=['GET'])
@main.route('/main',methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/signup',methods=['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template('signup.html')
    else :
        pass