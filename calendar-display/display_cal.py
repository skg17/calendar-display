from flask import Flask, render_template
from quickstart import get_events_info
import datetime
import calendar

app = Flask(__name__)
month = datetime.datetime.now().month
year = datetime.datetime.now().year

def is_event_ongoing(start, end):
    now = datetime.datetime.now().replace(tzinfo="UTC+01:00")

    return start <= now <= end

def is_event_allday(start, end):
    return (start.hour == 0 and start.minute == 0 and end.hour == 0 and end.minute == 0)

def is_future_event(start):
    now = datetime.datetime.now()

    return now < start.replace(tzinfo=None)

def is_cam_on(event_name):
    cam_on_events = ["meeting", "interview", "pmt"]
    event_name = event_name.lower()
    cam = False

    for event in cam_on_events:
        if event in event_name:
            cam = True
    
    return cam

@app.route("/")
def index():
    events = get_events_info()
    all_day_events = [event for event in events if is_event_allday(event[0], event[1])]
    events = [event for event in events if event not in all_day_events]

    current_event = None
    future_events = []

    current_name, current_times, upcoming_event, cam = "No events currently", "", "No upcoming events", False

    for event in events:
        if is_event_ongoing(start=event[0], end=event[1]):
           current_event = event
           cam = is_cam_on(current_event[2])

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
                           all_day_events=all_day_events,
                           current_event_name=current_name, 
                           current_event_times=current_times, 
                           upcoming_event=upcoming_event,
                           cam=cam)
    
app.run(host="0.0.0.0", port=6969)