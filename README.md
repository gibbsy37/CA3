# CA3
## Introduction 
The purpose of this program is to create a user friendly covid-aware alarm clock that someone with a computer can keep up to date with the current weather, news and local covid information with the added functionality of allowing the person to set alarms in the day for this information to read aloud to them.
## Prerequisites
Lastest version of Python to be installed onto users computer (current lastest version Python 3.9),
Following Python modules to be installed onto user computer:
-flask
-wheel
-pyttsx3
-time
-sched
-logging
-json
-requests
-datetime
-uk_covid19,
Own news and weather API keys which can be accessed from following sites; https://newsapi.org/, https://openweathermap.org,
Stable internet connection required too.
## Installation
Following Python modules to be installed onto user computer through command prompt:
-flask
-wheel
-pyttsx3
-time
-sched
-logging
-json
-requests
-datetime
-uk_covid19
## Getting started tutorial
Run program on command prompt using following command "python main_sans_logging.py" in appropiate directory,
Navigate to internet page through following link; http://127.0.0.1:5000/,
User should input time they want alarm to go off to notify them of information and add label to alarm.
## Developer Documentation
NAME
    main_sans_logging

DESCRIPTION
    The purpose of this program is to create a user friendly covid-aware alarm clock that someone with a computer can keep up to date with the current weather, news and local       covid information with the added functionality of allowing the person to set alarms in the day for this information to read aloud to them.
FUNCTIONS
    alarm_delete() -> <built-in function any>
        Deletes alarm when requested and removes from queue

    announce(announcement)
        Allows computer to speak to user and uses try except statement in case of error

    controller() -> <built-in function any>
        Delay created after user inputs alarm
        When time comes for alarm to go off notifications are said to user

    main() -> <built-in function any>

    notification_delete() -> <built-in function any>
        Deletes notification when requested and moves from page

DATA
    alarms = []
    api = COVID-19 in the UK - API Service
    Current paramet...te\"}",
        "...
    app = <Flask 'main_sans_logging'>
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    cases_and_deaths = {'areaCode': 'areaCode', 'areaName': 'areaName', 'c...
    complete_url = 'http://api.openweathermap.org/data/2.5/weather?appid=8...
    config = <_io.TextIOWrapper name='./config.json' mode='r' encoding='cp...
    country = 'gb'
    engine = <pyttsx3.engine.Engine object>
    exeter_only = ['areaName=Exeter']
    json_data = {'data': [{'areaCode': 'E07000041', 'areaName': 'Exeter', ...
    location = 'Exeter'
    s = <sched.scheduler object>

## Details
Author: Adam Gilbert
Licence: file:///C:/Users/adamg/Documents/CA3%20Python%20Package/LICENSE.htm
Link to source: test
