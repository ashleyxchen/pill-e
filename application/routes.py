from symbol import yield_arg
from application import app
from flask import render_template
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home = True, time = date.today())

@app.route('/settings')
def settings():
    return render_template('settings.html', settings = True)