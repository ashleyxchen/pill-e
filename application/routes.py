import datetime
from hashlib import blake2b
from application import app
from flask import render_template, request, redirect, url_for, session, jsonify
from datetime import date, datetime
import datetime
import json

app.secret_key = "asdfghjkl"
numPills = 0
numDosage = 0

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
    
    with open('pill1Configs.json') as pill1Config_file:
        pill1Configs = json.load(pill1Config_file)
        pill1Name = pill1Configs['pill1Name']
        pill1Time = pill1Configs['time1']
        pill1Config_file.close()
    
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    print("this is min", min)
    pill1Hour = pill1Time[0:2]
    pill1Hour = int(pill1Hour)
    pill1Min = pill1Time[3]
    pill1Min = int(pill1Min)
    status1 = "Due"
    if hour >= pill1Hour:
        if min > pill1Min:
            status1 = "Dispensed"        

    with open('pill2Configs.json') as pill2Config_file:
        pill2Configs = json.load(pill2Config_file)
        pill2Name = pill2Configs['pill2Name']
        pill2Time = pill2Configs['time']
        pill2Config_file.close()
    

    pill2Hour = pill2Time[0:2]
    print(pill2Hour)
    pill2Hour = int(pill2Hour)
    pill2Min = pill2Time[3]
    pill2Min = int(pill2Min)
    print(pill2Min)
   
    status2 = "Due"
    if hour >= pill2Hour:
        if min > pill1Min:
            status2 = "Dispensed"
        

    return render_template('home.html', home = True, 
    pill1Name = pill1Name, 
    pill1Time=pill1Time, 
    month = month, 
    dateApd = dateApd, 
    time = date.today(), 
    status1 = status1,
    status2=status2,
    pill2Name=pill2Name,
    pill2Time=pill2Time
    )

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    pill1Name = ""
    pill2Name = ""

    pill1Configs = {}
    pill1Config_file = open('pill1Configs.json', 'r')
    pill1Configs = json.load(pill1Config_file)
    pill1Name = pill1Configs['pill1Name']
    pill1Count = pill1Configs['pill1Count']
    pill1Dosage = pill1Configs['pill1Dosage']
    pill1Config_file.close()
    

    pill2Configs = {}
    pill2Config_file = open('pill2Configs.json', 'r')
    pill2Configs = json.load(pill2Config_file)
    pill2Name = pill2Configs['pill2Name']
    pill2Count = pill2Configs['pillCount']
    pill2Dosage = pill2Configs['pillDosage']
    pill2Config_file.close()
    
   
    return render_template("settings.html", settings=True, 
    pill1Name=pill1Name, 
    pill2Name=pill2Name,
    pill1Count= pill1Count,
    pill1Dosage = pill1Dosage,
    pill2Count=pill2Count,
    pill2Dosage=pill2Dosage)
    

@app.route('/pill1', methods=['GET', 'POST'])
def pill1():
    pill1Count = 0
    pill1Dosage = 0
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
            print(pill1Dosage)
            pill1Configs['pill1Dosage'] = pill1Dosage
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
        
        pill1Configs['tuesday1'] = bool(request.form.get('tuesday1'))

        pill1Configs['wednesday1'] = bool(request.form.get('wednesday1'))

        pill1Configs['thursday1'] = bool(request.form.get('thursday1'))

        pill1Configs['friday1'] = bool(request.form.get('friday1'))

        pill1Configs['saturday1'] = bool(request.form.get('saturday1'))

        pill1Configs['sunday1'] = bool(request.form.get('sunday1'))

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

    if request.method == 'POST': 
        pill2Configs = {}
        pill2Config_file = open('pill2Configs.json', 'r')
        pill2Configs = json.load(pill2Config_file)
        pill2Config_file.close()
        print(request.form.keys())

        if 'pill2Count' in request.form.keys():
            pill2Count = int(request.form['pillCount'])
            print(pill2Count)
            pill2Configs['pillCount'] = pill2Count
        else: pill2Count = pill2Configs['pillCount'] 

        if 'pill2Dosage' in request.form.keys():
            pill2Dosage = int(request.form['pill2Dosage'])
            print(pill2Dosage)
            pill2Configs['pillDosage'] = pill2Dosage
        else: pill2Dosage = pill2Configs['pillDosage'] 

        if 'pill2Name' in request.form.keys():
            pill1Name = request.form.get('pill2Name')
            print(pill1Name)
            pill2Configs['pill2Name'] = pill1Name
        else: pill2Name = pill2Configs['pill2Name'] 

        if 'time2' in request.form.keys():
            time2 = request.form.get('time2')
            print(time2)
            pill2Configs['time2'] = str(time2)
        else: 
            time = pill2Configs['time']
            print(time)

        pill2Configs['monday'] = bool(request.form.get('monday'))
        
        pill2Configs['tuesday'] = bool(request.form.get('tuesday'))

        pill2Configs['wednesday'] = bool(request.form.get('wednesday'))

        pill2Configs['thursday'] = bool(request.form.get('thursday'))

        pill2Configs['friday'] = bool(request.form.get('friday'))

        pill2Configs['saturday'] = bool(request.form.get('saturday'))

        pill2Configs['sunday'] = bool(request.form.get('sunday'))

        pill2Config_file.close()

        print(pill2Configs)
        
        pill2Config_file = open('pill2Configs.json', 'w')
        json.dump(pill2Configs, pill2Config_file)
        pill2Config_file.close()

        session[request.form['pillCount']] = True
        session[request.form['pillDosage']] = True
        session[request.form['pill2Name']] = True
        session[request.form['time']] = True

    # if request.method == 'POST': 
    #     pill1Name = request.form["pill1Name"]
    #     return redirect(url_for('settings',settings=True, pill1Name=pill1Name))
    return render_template('pill2.html', pill2 = True, pill2Name=pill2Name)

# @app.before_first_request
# def checkSchedule():
#     while True:
#         pill1Name = ""
#         pill2Name = ""

#         now = datetime.now()
#         current_time = now.strftime("%H:%M")
#         today = date.today()
#         datetime.datetime.today()
#         datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
#         weekday = datetime.datetime.today().weekday()

#         pill1Configs = {}
#         pill1Config_file = open('pill1Configs.json', 'r')
#         pill1Configs = json.load(pill1Config_file)
#         pill1Config_file.close()
#         pill1Name = pill1Configs['pill1Name']
#         time1 = pill1Configs['time1']
#         monday1 = pill1Configs['monday1']
#         tuesday1 = pill1Configs['tuesday1']
#         wednesday1 = pill1Configs['wednesday1']
#         thursday1 = pill1Configs['thursday1']
#         friday1 = pill1Configs['friday1']
#         saturday1 = pill1Configs['saturday1']
#         sunday1 = pill1Configs['sunday1']

        

#         if (time1 == str(current_time)):
#             if (monday1 == True) and (weekday == "0"):
#                 print("Current Time =", current_time)
#             if (tuesday1 == True) and (weekday == "1"):
#                 print("Current Time =", current_time)
#             if (wednesday1 == True) and (weekday == "2"):
#                 print("Current Time =", current_time)
#             if (thursday1 == True) and (weekday == "3"):
#                 print("Current Time =", current_time)
#             if (friday1 == True) and (weekday == "4"):
#                 print("Current Time =", current_time)
#             if (saturday1 == True) and (weekday == "5"):
#                 print("Current Time =", current_time)
#             if (sunday1 == True) and (weekday == "6"):
#                 print("Current Time =", current_time)


#         pill2Configs = {}
#         pill2Config_file = open('pill2Configs.json', 'r')
#         pill2Configs = json.load(pill2Config_file)
#         pill2Config_file.close()
#         pill2Name = pill2Configs['pill2Name']
#         time = pill2Configs['time']
#         monday = pill1Configs['monday']
#         tuesday = pill1Configs['tuesday']
#         wednesday = pill1Configs['wednesday']
#         thursday = pill1Configs['thursday']
#         friday = pill1Configs['friday']
#         saturday = pill1Configs['saturday']
#         sunday = pill1Configs['sunday']

#         if (time1 == str(current_time)):
#             if (monday == True) and (weekday == "0"):
#                 print("Current Time =", current_time)
#             if (tuesday == True) and (weekday == "1"):
#                 print("Current Time =", current_time)
#             if (wednesday == True) and (weekday == "2"):
#                 print("Current Time =", current_time)
#             if (thursday == True) and (weekday == "3"):
#                 print("Current Time =", current_time)
#             if (friday == True) and (weekday == "4"):
#                 print("Current Time =", current_time)
#             if (saturday == True) and (weekday == "5"):
#                 print("Current Time =", current_time)
#             if (sunday == True) and (weekday == "6"):
#                 print("Current Time =", current_time)

    