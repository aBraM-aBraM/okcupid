# OKCUPID

okcupid automation

## Setup

Setup for production environments is easiest using compose.
You can edit `.env` to your likings

``` bash
docker compose up -d
```

For development / hacking a local setup can be done too

```
pip3 install -r requirements.txt

# to start sending messages usign your session
# session_file should contain your okcupid session
python3 okcupid/main.py --session SESSION_FILE

# start the telegram bot
python3 telegram/main.py
```
