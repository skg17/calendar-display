from flask import Flask, render_template
from quickstart import get_events_info
import datetime
import calendar

app = Flask(__name__)
month = datetime.datetime.now().month
year = datetime.datetime.now().year

def is_event_ongoing(start, end):
    now = datetime.datetime.now()

    return start.replace(tzinfo=None) <= now <= end.replace(tzinfo=None)

def is_future_event(start):
    now = datetime.datetime.now()

    return now < start.replace(tzinfo=None)

@app.route("/")
def index():
    events = get_events_info()
    current_event = None
    future_events = []

    for event in events:
        if is_event_ongoing(start=event[0], end=event[1]):
           current_event = event

        if is_future_event(start=event[0]):
            future_events.append(event)

    return current_event

app.run(host="0.0.0.0", port=6969)