from application import app
from flask import render_template, request, redirect, url_for, session
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    monthNum = date.today().month
    if monthNum == 1:
        month='Jan'
    elif monthNum == 2:
        month = 'Feb'
    elif monthNum == 3:
        month = 'Mar'
    elif monthNum == 4:
        month = 'Apr'
    elif monthNum == 5:
        month = 'May'
    elif monthNum == 6:
        month = 'Jun'
    elif monthNum == 7:
        month = 'Jul'
    elif monthNum == 8:
        month = 'Aug'
    elif monthNum == 9:
        month = 'Sept'
    elif monthNum == 10:
        month = 'Oct'
    elif monthNum == 11:
        month = 'Nov'
    elif monthNum == 12:
        month = 'Dec'
    
    dateNum = date.today().day
    print(dateNum)
    if dateNum == 1 or dateNum == 11 or dateNum == 21 or dateNum == 31:
        dateApd = 'st'
    elif dateNum == 2 or dateNum == 12 or dateNum == 22:
        dateApd = 'nd'
    elif dateNum == 3 or dateNum == 13 or dateNum == 23:
        dateApd = 'rd'
    else:
        dateApd = 'th'
    

    return render_template('home.html', home = True, month = month, dateApd = dateApd, time = date.today())

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

  
    