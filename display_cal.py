from flask import Flask, render_template
from quickstart import get_events_info
import datetime
import calendar

app = Flask(__name__)
month = datetime.datetime.now().month
year = datetime.datetime.now().year

@app.route("/")
def index():
    return get_events_info()

app.run(host="0.0.0.0", port=6969)