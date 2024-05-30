# Calendar Display
***Create a Web Interface to Display Google Calendar Events***
![main](https://github.com/skg17/calendar-display/assets/32193465/5bf59e57-1945-4129-8419-65d056e8d297)

This project displays your Google Calendar events on a locally hosted webpage. It fetches the ongoing event, the next upcoming event, and all-day events, presenting them in a clean, minimalist interface. The time and date are dynamically updated.

The repo also contains a Dockerfile, which will allow for containerization. In my case, I have deployed the Docker image on my CasaOS home server to have a display of my schedule for people to be aware of my working times!

## Features
- **Current Ongoing Event:** Displays the current ongoing event in the center of the page with the event times. Also displays a camera ( &#128247; ) emoji if event requires a webcam.
- **Next Upcoming Event:** Displays the next upcoming event at the bottom of the page with the event time.
- **All Day Events:** Automatically detects all-day events and displays them at the top right corner of the page, separate from timed events.
- **Current Time and Date:** Dynamically updated current time and date displayed in the top left corner.

## Prerequisites
- Python 3.6 or higher (developed using Python 3.12)
- Google Calendar API credentials
- Docker (optional, for containerization)
- CasaOS (optional, for deployment on a home server)

## Installation
### Local Setup
1. **Clone this repository:**
    ```bash
    git clone https://github.com/skg17/calendar-display.git
    cd calenday-display
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the Google Calendar API:**
    - Follow the [Google Calendar API Python Quickstart](https://developers.google.com/calendar/api/quickstart/python) to obtain `credentials.json`.
    - Move `credentials.json` to the `calendar-display` sub-directory.
5. **Run the script:**
    ```bash
    python calendar-display.py
    ```
    Upon first running the program, you may be asked to sign into Google Calendar to generate a token. After doing so once the prompt should not appear again.
    
    By default the script will create the webpage and display it on port 6969 of the local host, so the page can be found by navigating to `http://localhost:6969` on your browser of choice.

### Docker Setup (optional)
1. **Build the Docker image:**
    ```bash
    docker build -t calendar-display-docker .
    ```
2. **Run the Docker container:**
    ```bash
    docker run -d -p 6969:6969 calendar-display-docker
    ```
    Once again, the webpage will be available at `http://localhost:6969`.

### Deployment on CasaOS (optional)
As of yet, I haven't been able to get the installation working using CasaOS's built-in container installer. A work-around is highlighted here:
1. **Copy the repository to the AppData directory in CasaOS:**
    Simply drag and drop the repo folder, including `credentials.json` and `token.json`, into the AppData directory of your server.
2. **Create and run the Docker container:**
    From the CasaOS terminal, follow Steps 1-2 of the Docker Setup section.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
