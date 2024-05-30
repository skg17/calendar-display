import datetime
import os.path
import google
import calendar

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def get_events_info():
  """
  Returns a list containing all the events in the current day.

  Returns:
  --------
    events_info (list) : list containing sublists made of an event's start and end time, and its name.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    day = datetime.datetime.now().day

    # Call the Calendar API
    start = datetime.datetime(year, month, day).isoformat() + "Z"
    end = datetime.datetime(year, month, day+1).isoformat() + "Z"

    events_info = []

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start,
            timeMax=end,
        )
        .execute()
    )
    events = events_result.get("items", [])

    # Gather data for list
    for event in events:
      # Stores event name
      try:
        event_name = event["summary"]
      # Unless event is untitled, in which case name is stored as 'Untitled Event'
      except:
        event_name = "Untitled Event"

      # Get event start and end times
      start = event["start"].get("dateTime", event["start"].get("date"))
      start = datetime.datetime.fromisoformat(start)
      end = event["end"].get("dateTime", event["end"].get("date"))
      end = datetime.datetime.fromisoformat(end)

      # Adds info to sub-list which is appended to events_info list
      events_info.append([start, end, event_name])

    return events_info

  except HttpError as error:
    print(f"An error occurred: {error}")

def is_event_ongoing(start, end):
  """
  Checks if an event is ongoing by comparing the current time to the event start and end times.

  Parameters:
  -----------
    start (datetime) : the start time of the specified event.
    end (datetime) : the end time of the specified event.

  Returns:
  --------
    (bool) : whether the given event is ongoing or not.
  """
  return start.replace(tzinfo=None) <= datetime.datetime.now() <= end.replace(tzinfo=None)

def is_event_allday(start, end):
  """
  Checks if an event lasts all day by checking if both the start and end times are midnight.

  Parameters:
  -----------
    start (datetime) : the start time of the specified event.
    end (datetime) : the end time of the specified event.

  Returns:
  --------
    (bool) : whether the given event lasts all day or not.
  """
  return start.hour == 0 and start.minute == 0 and end.hour == 0 and end.minute == 0

def is_future_event(start):
  """
  Checks if an event is upcoming by comparing the start time against current time.

  Parameters:
  -----------
    start (datetime) : the start time of the specified event.

  Returns:
  --------
    (bool) : whether the given event is upcoming or not.
  """
  return datetime.datetime.now() < start.replace(tzinfo=None)

def is_cam_on(event_name):
  """
  Checks if an event requires a webcam by looking for specific words in the event name.

  Parameters:
  -----------
    event_name (str) : the name of the specified event.

  Returns:
  --------
    (bool) : whether the given event is requires a webcam or not.
  """
  # cam_on_events is a list of strings that when found in the event name indicate the need for a cam
  cam_on_events = ["meeting", "interview", "pmt", "webcam", "camera"]

  # Returns whether any keyword was found in the event name
  return any([keyword in event_name.lower() for keyword in cam_on_events])