from application import app
from flask import render_template, request, redirect, url_for
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home = True, time = date.today())

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    pill1Name = request.form.get('pill1Name')
    print(pill1Name)
    return render_template("settings.html", settings=True, pill1Name=pill1Name)
    

@app.route('/pill1')
def pill1():
    if request.method == 'POST': 
        pill1Name = request.form["pill1Name"]
        return redirect(url_for('settings',settings=True, pill1Name=pill1Name))
    return render_template('pill1.html')
    