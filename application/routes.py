from hashlib import blake2b
from application import app
from flask import render_template, request, redirect, url_for, session, jsonify
from datetime import date
import json

app.secret_key = "asdfghjkl"
numPills = 0
numDosage = 0

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home = True, time = date.today())

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    pill1Configs = {}
    with open('pill1Configs.json') as pill1Config_file:
        pill1Configs = json.load(pill1Config_file)
        pill1Name = pill1Configs['pill1Name']
        pill1Config_file.close()

    with open('pill2Configs.json') as pill2Config_file:
        pill2Configs = json.load(pill2Config_file)
        pill2Name = pill2Configs['pill2Name']
        pill2Config_file.close()
   
    return render_template("settings.html", settings=True, pill1Name=pill1Name, pill2Name=pill2Name)
    

@app.route('/pill1', methods=['GET', 'POST'])
def pill1():
    pillCount = 0
    pillDosage = 0
    pill1Name = ""
    
    if request.method == 'POST': 
        pill1Configs = {}
        pill1Config_file = open('pill1Configs.json', 'r')
        pill1Configs = json.load(pill1Config_file)
        pill1Config_file.close()
        print(request.form.keys())

        if 'pill1Count' in request.form.keys():
            pill1Count = int(request.form['pill1Count'])
            print(pill1Count)
            pill1Configs['pill1Count'] = pill1Count
        else: pill1Count = pill1Configs['pill1Count'] 

        if 'pill1Dosage' in request.form.keys():
            pill1Dosage = int(request.form['pill1Dosage'])
            print(pillDosage)
            pill1Configs['pillDosage'] = pill1Dosage
        else: pill1Dosage = pill1Configs['pill1Dosage'] 

        if 'pill1Name' in request.form.keys():
            pill1Name = request.form.get('pill1Name')
            print(pill1Name)
            pill1Configs['pill1Name'] = pill1Name
        else: pill1Name = pill1Configs['pill1Name'] 

        # not entering this if statement therefore not passed into json and stored
        if 'time1' in request.form.keys():
            time1 = request.form.get('time1')
            print(time1)
            pill1Configs['time1'] = str(time1)
        else: 
            time1 = pill1Configs['time1']
            print(time1)

        pill1Configs['monday1'] = bool(request.form.get('monday1'))
        

        tuesday1 = request.form.get('tuesday1')
        pill1Configs['tuesday1'] = bool(tuesday1)

        wednesday1 = request.form.get('wednesday1')
        if wednesday1: pill1Configs['wednesday1'] = bool(wednesday1)
        else: pill1Configs['wednesday1'] = False

        thursday1 = request.form.get('thursday1')
        if thursday1: pill1Configs['thursday1'] = bool(thursday1)
        else: pill1Configs['thursday1'] = False

        friday1 = request.form.get('friday1')
        if friday1: pill1Configs['friday1'] = bool(friday1)
        else: pill1Configs['friday1'] = False

        saturday1 = request.form.get('saturday1')
        if saturday1:pill1Configs['saturday1'] = bool(saturday1)
        else: pill1Configs['saturday1'] = False

        sunday1 = request.form.get('sunday1')
        if sunday1: pill1Configs['sunday1'] = bool(sunday1)
        else: pill1Configs['sunday1'] = False

        print(pill1Configs)
        
        pill1Config_file = open('pill1Configs.json', 'w')
        json.dump(pill1Configs, pill1Config_file)
        pill1Config_file.close()

        session[request.form['pill1Count']] = True
        session[request.form['pill1Dosage']] = True
        session[request.form['pill1Name']] = True
        session[request.form['time1']] = True

        

        
    # if request.method == 'POST': 
    #     pill1Name = request.form["pill1Name"]
    #     return redirect(url_for('settings',settings=True, pill1Name=pill1Name))
    return render_template('pill1.html', pill1Name=pill1Name, pill1 = True)
    



@app.route('/pill2', methods=['GET', 'POST'])
def pill2():
    pill2Count = 0
    pill2Dosage = 0
    pill2Name = ""
    with open('pill2Configs.json', 'r+') as pill2Config_file:
        pill2Configs = json.load(pill2Config_file)
        pill2Name = pill2Configs['pill2Name']
        pill2Config_file.close()

    if request.method == 'POST': 
        pill2Configs = {}
        with open('pill2Configs.json') as pill2Config_file:
            pill2Configs = json.load(pill2Config_file)
            pill2Name = pill2Configs['pill2Name'] 

            if 'pill2Count' == request.form.keys():
                pill2Count = int(request.form['pillCount'])
                print(pill2Count)
                pill2Configs['pillCount'] = pill2Count
            else: pill2Count = pill2Configs['pillCount'] 
            

            if 'pill2Dosage' == request.form.keys():
                pill2Dosage = int(request.form['pill2Dosage'])
                print(pill2Dosage)
                pill2Configs['pillDosage'] = pill2Dosage
            else: pill2Dosage = pill2Configs['pillDosage'] 

            if 'pill2Name' == request.form.keys():
                pill1Name = request.form.get('pill2Name')
                print(pill1Name)
                pill2Configs['pill2Name'] = pill1Name
            else: pill2Name = pill2Configs['pill2Name'] 

            # not entering this if statement therefore not passed into json and stored
            if 'time2' == request.form.keys():
                time2 = request.form.get('time2')
                print(time2)
                pill2Configs['time2'] = str(time2)
            else: 
                time = pill2Configs['time']
                print(time)

            monday = request.form.get('monday')
            if monday: pill2Configs['monday'] = bool(monday)
            else: pill2Configs['monday'] = False

            tuesday = request.form.get('tuesday')
            if tuesday: pill2Configs['tuesday'] = bool(tuesday)
            else: pill2Configs['tuesday'] = False

            wednesday = request.form.get('wednesday')
            if wednesday: pill2Configs['wednesday'] = wednesday
            else: pill2Configs['wednesday'] = False

            thursday = request.form.get('thursday')
            if thursday: pill2Configs['thursday'] = thursday
            else: pill2Configs['thursday'] = False

            friday = request.form.get('friday')
            if friday: pill2Configs['friday'] = friday
            else: pill2Configs['friday'] = False

            saturday = request.form.get('saturday')
            if saturday:pill2Configs['saturday'] = saturday
            else: pill2Configs['saturday'] = False

            sunday = request.form.get('sunday')
            if sunday: pill2Configs['sunday'] = sunday
            else: pill2Configs['sunday'] = False

            pill2Config_file.close()

        with open('pill2Configs.json', 'w') as pill2Config_file:
            json.dump(pill2Configs, pill2Config_file)
            session[request.form['pillCount']] = True
            session[request.form['pillDosage']] = True
            session[request.form['pill2Name']] = True
            session[request.form['time']] = True

    # if request.method == 'POST': 
    #     pill1Name = request.form["pill1Name"]
    #     return redirect(url_for('settings',settings=True, pill1Name=pill1Name))
    return render_template('pill2.html', pill2 = True, pill2Name=pill2Name)
    