# coding: utf8

from blogapp import app
from flask import render_template, redirect, flash
from .forms import LoginForm

@app.route('/index')
def index():
    user = {'nickname': 'Stone'} # fake

    # posts
    posts = [
        {
            'author': {'nickname':'John'},
            'body':'Beautiful day in Poland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The movie was so cool.'
        }
    ]
    return render_template('index.html',   
        title = 'Home',     
        user = user,
        posts = posts)



@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login required for openid:' + form.openid.data + \
            ', remember_me=' + str(form.remember_me.data))
        return redirect('/index')

    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])