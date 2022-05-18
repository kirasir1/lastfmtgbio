import json, requests, configparser, time, getpass
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync, errors, functions, types
config = configparser.ConfigParser()
config.read('tgapi.cfg')
api_id = config['tg_api_creds']['api_id']
api_hash = config['tg_api_creds']['api_hash']
user = config['lastfm_creds']['user']
api_key = config['lastfm_creds']['api_key']
updatedbio=''
playingnow=''
client = TelegramClient('botbio', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    phone = input("Enter phone: ")
    client.send_code_request(phone)
    value = input("Enter code: ")
    answer = input('Do you have 2FA password on account? (yes/no) ')
    if answer.lower() in ['y', 'yes']:
        password = getpass.getpass(prompt='Enter password: ')
        client.sign_in(phone)
        try:
            client.sign_in(code=value)
        except SessionPasswordNeededError:
            client.sign_in(password=password)
    else:
        client.sign_in(code=value)
while True:
    try:
        url = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&limit=1&user={user}&api_key={api_key}&format=json')
    except Exception as e:
        print(e)
        pass
    lastfmjson = url.json()
    artist=lastfmjson["recenttracks"]["track"][0]["artist"]['#text']
    album=lastfmjson["recenttracks"]["track"][0]['name']
    try:
        playingnow=lastfmjson["recenttracks"]["track"][0]["@attr"]['nowplaying']
    except Exception as e:
        print(e)
        pass
    if playingnow=='true':
        bio='▶️ Playing: '+artist+' — '+album
    else:
        bio='⏸ Last track: '+artist+' — '+album
    if updatedbio!=bio:
        try:
            from telethon.tl.functions.account import UpdateProfileRequest
            result = client(functions.account.UpdateProfileRequest(about=bio))
            print('Bio has been updated:', bio)
            updatedbio=bio
            time.sleep(30)
        except Exception as e:
            print(e)
            pass
    else:
        time.sleep(15)
