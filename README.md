# Calendar Display
***Create a Web Interface to Display Google Calendar Events***

This project displays your Google Calendar events on a locally hosted webpage. It fetches the ongoing event, the next upcoming event, and all-day events, presenting them in a clean, minimalist interface. The time and date are dynamically updated.

The repo also contains a Dockerfile, which will allow for containerization. In my case, I have deployed the Docker image on my CasaOS home server to have a display of my schedule for people to be aware of my working times!

### Features
- **Current Ongoing Event:** Displays the current ongoing event in the center of the page with the event times. Also displays a camera ( &#128247; ) emoji if event requires a webcam.
- **Next Upcoming Event:** Displays the next upcoming event at the bottom of the page with the event time.
- **All Day Events:** Automatically detects all-day events and displays them at the top right corner of the page, separate from timed events.
- **Current Time and Date:** Dynamically updated current time and date displayed in the top left corner.

### Prerequisites
- Python 3.6 or higher (developed using Python 3.12)
- Google Calendar API credentials
- Docker (optional, for containerization)
- CasaOS (optional, for deployment on a home server)

### Installation
#### Local Setup
1. **Clone this repository:**
    ```bash
    git clone https://github.com/skg17/calendar-display.git
    cd calenday-display
    ```
