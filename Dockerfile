FROM python:3.12

WORKDIR /flask-app

COPY . .
RUN pip install -r requirements.txt

WORKDIR /flask-app/calendar-display

CMD [ "python3", "display_cal.py" ]