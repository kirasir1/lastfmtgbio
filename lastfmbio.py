import json, requests, time
from telethon import TelegramClient, events, sync
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
i=1
updatedbio=''
playingnow=''
while i>0:
    url = requests.get('http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&limit=1&user=YOUR_NICKNAME&api_key=YOUR_API_KEY&format=json')
    lastfmjson = url.json()
    artist=lastfmjson["recenttracks"]["track"][0]["artist"]['#text']
    album=lastfmjson["recenttracks"]["track"][0]['name']
    try:
        playingnow=lastfmjson["recenttracks"]["track"][0]["@attr"]['nowplaying']
    except:
        pass
    if playingnow=='true':
        bio='▶️ Playing: '+artist+' — '+album
    else:
        bio='⏸ Last track: '+artist+' — '+album
    if updatedbio!=bio:
        try:
            with TelegramClient('botbio', api_id, api_hash) as client:
                from telethon.tl.functions.account import UpdateProfileRequest
                client(
                    UpdateProfileRequest(about=bio
                    ))
            print('Bio updated:', bio)
            updatedbio=bio
            time.sleep(30)
        except:
            pass
    else:
        time.sleep(15)
