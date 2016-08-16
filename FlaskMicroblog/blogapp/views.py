# coding: utf8

from blogapp import app

@app.route('/')
def index():
    return '<h1>Hello World</h1>'