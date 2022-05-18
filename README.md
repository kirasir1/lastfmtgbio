# lastfmtgbio
This script sends your last scrobbled track from Last.FM to your Telegram page in bio.
# Requirements
- Telethon
- Requests
- Python 3
# How to start up
- Go to https://my.telegram.org, log in and go to "API development tools" page. Create app and save your app api_id api_hash
- Go to https://last.fm/bio and click "Get an API account". Save API key.
- Open `tgapi.cfg.sample` file and insert your credentials.
- Rename file to `tgapi.cfg`
- Get the required modules: `pip install -r requirements.txt`
- Run the script with command `python lastfmbio.py`
