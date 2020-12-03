from time_conversions import hhmm_to_seconds
from time_conversions import current_time_hhmm
from flask import Flask
from flask import request
from flask import render_template
import pyttsx3
import time
import sched
import logging
import json
import requests
from datetime import date
from uk_covid19 import Cov19API

config = open(r'./config.json', 'r')
config_json = json.load(config)

logging.basicConfig(filename=config_json['filepaths']['system_log'], encoding='utf-8', level=logging.DEBUG)

s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
logging.info(app)
engine = pyttsx3.init()
notifications = []
alarms = []

base_url = "https://newsapi.org/v2/top-headlines?"
api_key = config_json["apikeys"]["news"]
country = "gb"
complete_url = base_url + "country=" + country + "&apiKey=" + api_key
response = requests.get(complete_url).json()
articles = response["articles"]
news = []
for article in articles[0:3]:
    d = {'title': article['title'], 'content': article['description']}
    news.append(d)

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = config_json["apikeys"]["weather"]
location = config_json["location"]
complete_url = base_url + "appid=" + api_key + "&q=" + location
response = requests.get(complete_url).json()
weather = response["weather"]
weather_status = []
for w in weather:
    d = {'title': w['main'], 'content': w['description']}
    weather_status.append(d)

exeter_only = [
    'areaName={}'.format(config_json['location'])
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(filters=exeter_only, structure=cases_and_deaths, latest_by="newCasesByPublishDate")

json_data = api.get_json()
covid = json_data["data"]

covid_info = []
d = {'title': "Covid information", 'content': covid}
covid_info.append(d)

notifications = news + weather_status + covid_info


@app.route('/')
def main() -> any:
    s.run(blocking=False)
    alarm_time = request.args.get("alarm")
    return controller()


@app.route('/index')
def controller() -> any:
    s.run(blocking=False)
    alarm_time = request.args.get("alarm")
    logging.info(alarm_time)
    if alarm_time:
        alarm_hhmm = alarm_time[-5:-3] + ':' + alarm_time[-2:]
        logging.info(alarm_hhmm)
        today = date.today()
        alarm_date = alarm_time[:10]
        delay = hhmm_to_seconds(alarm_hhmm) - hhmm_to_seconds(current_time_hhmm())
        update = request.args.get("two")
        alarms.append({'time': alarm_time, 'content': update})
        s.enter(int(delay), 1, announce, [notifications[0]['title'], ])
    alarm_item = request.args.get("alarm_item")
    print(alarm_item)
    return render_template('index.html', title='Daily update', notifications=notifications,
                           image='alarm-meme.jpg', alarms=alarms)


@app.route('/alarm_delete')
def alarm_delete() -> any:
    alarm_item = request.args.get("alarm_item")
    queue = s.queue
    for item in queue:
        time_check = list(item)
        if int(time_check[0]) == time.mktime(time.strptime(str(alarm_item), "%Y-%m-%dT%H:%M")):
            s.cancel(item)
            print(queue)
    for item in alarms:
        if item['time'] == request.args.get("alarm_item"):
            alarms.remove(item)
    return controller()


@app.route('/notification_delete')
def notification_delete():
    notification_item = request.args.get("notif")
    for item in notifications:
        if item['title'] == notification_item:
            notifications.remove(item)
    return controller()


def announce(announcement):
    try:
        engine.endLoop()
    except:
        logging.error(announcement)
        pass
    engine.say(announcement)
    engine.runAndWait()


if __name__ == '__main__':
    app.run()

