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
logging.basicConfig(filename='sys1.log', encoding='utf-8', level=logging.DEBUG)

s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
logging.info(app)
engine = pyttsx3.init()
notifications = []
alarms = []

""""@app.route('/alarm_setting')
def alarm_setting():
    alarm_time = request.args.get("alarm")
    tr = threading.Thread(target=s.run)
    tr.daemon = True
    tr.start()
    return index()"""

@app.route('/')
def controller():
    s.run(blocking=False)
    alarm_time = request.args.get("alarm")
    print(s.queue)
    logging.info(alarm_time)
    print(alarm_time)
    bbc_news = json.load(open('bbc_news.json', 'r'))
    weather = json.load(open('weather.json', 'r'))
    notifications = bbc_news + weather
    if alarm_time:
        alarm_hhmm = alarm_time[-5:-3] + ':' + alarm_time[-2:]
        logging.info(alarm_hhmm)
        delay = hhmm_to_seconds(alarm_hhmm) - hhmm_to_seconds(current_time_hhmm())
        update = request.args.get("two")
        alarms.append({'time': alarm_time, 'content': update})
        s.enter(int(delay), 1, announce, [notifications[0]['title'], ])
        s.enter(int(delay), 2, announce, [notifications[1]['title'], ])
        s.enter(int(delay), 3, announce, [notifications[2]['title'], ])
        s.enter(int(delay), 4, announce, [notifications[3]['content'], ])
    return render_template('index.html', title='Daily update', notifications=notifications, alarms=alarms,
                           image='alarm-meme.jpg')


"""def cancel_alarms():
    if alarm == alarm['title']:"""


"""def restore_state():
    with open('sys1.log') as logfile:
        restore_alarms=[]
        for line in logfile.readlines():
            if line[:4] == 'INFO' and line[-7:-1] == 'Set alarms':
                args = line.split(',')
                if alarm_time#if alarm time in the future - this command needs to be implemented
                    restore_alarms.append((args[-4], args[-3], args[-2], args[-1][:-1]))
    [set_alarm(al[0], al[1], al[2], al[3], False) for al in restore_alarms]"""

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