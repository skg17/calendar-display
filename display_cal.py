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

    current_name, current_times, upcoming_event = "No events currently", "", "No upcoming events"

    for event in events:
        if is_event_ongoing(start=event[0], end=event[1]):
           current_event = event

        if is_future_event(start=event[0]):
            future_events.append(event)

    if current_event:
        current_name = current_event[2].title()
        current_start = "{0}:{1:02d}".format(current_event[0].hour, current_event[0].minute)
        current_end = "{0}:{1:02d}".format(current_event[1].hour, current_event[1].minute)
        current_times = "({0} - {1})".format(current_start, current_end)

    if future_events:
        future_name = future_events[0][2].title()
        future_start = "{0}:{1:02d}".format(future_events[0][0].hour, future_events[0][0].minute)
        future_end = "{0}:{1:02d}".format(future_events[0][1].hour, future_events[0][1].minute)
        upcoming_event = "({0} - {1}) {2}".format(future_start, future_end, future_name)

    return render_template("template.html", 
                           current_event_name=current_name, 
                           current_event_times=current_times, 
                           upcoming_event=upcoming_event)
    
app.run(host="0.0.0.0", port=6969)