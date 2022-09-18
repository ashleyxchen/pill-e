from application import app
from flask import render_template, request, redirect, url_for, session, jsonify
from datetime import date
import json
import os.path

app.secret_key = "asdfghjkl"
numPills = 0
numDosage = 0

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home = True, time = date.today())

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    pillCount = 0
    pillDosage = 0

    if request.method == 'POST': 
        pillConfigs = {}
        with open('pillConfigs.json') as pillConfig_file:
            pillConfigs = json.load(pillConfig_file)

            if 'pillCount' == request.form.keys():
                pillCount = int(request.form['pillCount'])
                print(pillCount)
                pillConfigs['pillCount'] = pillCount
            else: pillCount = pillConfigs['pillCount'] 
            

            if 'pillDosage' == request.form.keys():
                pillDosage = int(request.form['pillDosage'])
                print(pillDosage)
                pillConfigs['pillDosage'] = pillDosage
            else: pillDosage = pillConfigs['pillDosage'] 

            if 'pill1Name' == request.form.keys():
                pill1Name = request.form.get('pill1Name')
                print(pill1Name)
                pillConfigs['pill1Name'] = pill1Name
            else: pill1Name = pillConfigs['pill1Name'] 

            # not entering this if statement therefore not passed into json and stored
            if 'time' == request.form.keys():
                time = request.form.get('time')
                print(time)
                pillConfigs['time'] = str(time)
            else: 
                time = pillConfigs['time']
                print(time)

            monday = request.form.get('monday')
            if monday: pillConfigs['monday'] = bool(monday)
            else: pillConfigs['monday'] = False

            tuesday = request.form.get('tuesday')
            if tuesday: pillConfigs['tuesday'] = bool(tuesday)
            else: pillConfigs['tuesday'] = False

            wednesday = request.form.get('wednesday')
            if wednesday: pillConfigs['wednesday'] = wednesday
            else: pillConfigs['wednesday'] = False

            thursday = request.form.get('thursday')
            if thursday: pillConfigs['thursday'] = thursday
            else: pillConfigs['thursday'] = False

            friday = request.form.get('friday')
            if friday: pillConfigs['friday'] = friday
            else: pillConfigs['friday'] = False

            saturday = request.form.get('saturday')
            if saturday:pillConfigs['saturday'] = saturday
            else: pillConfigs['saturday'] = False

            sunday = request.form.get('sunday')
            if sunday: pillConfigs['sunday'] = sunday
            else: pillConfigs['sunday'] = False

            pillConfig_file.close()

        with open('pillConfigs.json', 'w') as pillConfig_file:
            json.dump(pillConfigs, pillConfig_file)
            session[request.form['pillCount']] = True
            session[request.form['pillDosage']] = True
            session[request.form['pill1Name']] = True
            session[request.form['time']] = True

    return render_template("settings.html", settings=True, pill1Name=pill1Name)
    

@app.route('/pill1')
def pill1():
    if request.method == 'POST': 
        pill1Name = request.form["pill1Name"]
        return redirect(url_for('settings',settings=True, pill1Name=pill1Name))
    return render_template('pill1.html')
    