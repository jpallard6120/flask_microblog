from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Hi doodzors'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'Hi doodzettez'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)