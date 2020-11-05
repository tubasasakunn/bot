from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime as dt
import random
# If modifying these scopes, delete the file token.pickle.
reply_list=[]
poem_list=[]
apology_list=[]
praise_list=[]
full_path='Documents/bot/bot/'

f = open(full_path+"reply_list.txt","r")
for x in f:
    reply_list.append(int(x.rstrip("\n")))
f.close()

f = open(full_path+"poem.txt","r")
for x in f:
    poem_list.append(x.rstrip("\n"))
f.close()

f = open(full_path+"apology.txt","r")
for x in f:
    apology_list.append(x.rstrip("\n"))
f.close()

f = open(full_path+"praise.txt","r")
for x in f:
    praise_list.append(x.rstrip("\n"))
f.close()


print('start')
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_event(date):
    
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    date=datetime.datetime.strptime(date, '%Y-%m-%d').isoformat()+'Z'

    events_result = service.events().list(calendarId='primary', timeMin=date,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    text=''
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        text=text+start[:10]+' '+start[11:16]+' '+event['summary']+'\n'
    return text
token='MLBMUAUC3D7BDA5KBJR7QPQ4C3D5M4XD'
import urllib.request
import ast

def get_age():
    info='https://api.ouraring.com/v1/userinfo?access_token='+token
    with urllib.request.urlopen(info) as response:
        info = response.read()
    info=ast.literal_eval(info.decode())
    return str(info['age'])

def get_height():
    info='https://api.ouraring.com/v1/userinfo?access_token='+token
    with urllib.request.urlopen(info) as response:
        info = response.read()
    info=ast.literal_eval(info.decode())
    return str(info['height'])

def get_weight():
    info='https://api.ouraring.com/v1/userinfo?access_token='+token
    with urllib.request.urlopen(info) as response:
        info = response.read()
    info=ast.literal_eval(info.decode())
    return str(info['weight'])

def get_bedtime_start(date):
    sleep='https://api.ouraring.com/v1/sleep?start='+date+'&end='+date+'&access_token='+token
    with urllib.request.urlopen(sleep) as response:
        sleep = response.read()
    sleep=ast.literal_eval(sleep.decode())
    bedtime_start=sleep['sleep'][0]['bedtime_start'][:10]+' '+sleep['sleep'][0]['bedtime_start'][11:16]
    return bedtime_start
    
def get_bedtime_end(date):
    sleep='https://api.ouraring.com/v1/sleep?start='+date+'&end='+date+'&access_token='+token
    with urllib.request.urlopen(sleep) as response:
        sleep = response.read()
    sleep=ast.literal_eval(sleep.decode())
    bedtime_end=sleep['sleep'][0]['bedtime_end'][:10]+' '+sleep['sleep'][0]['bedtime_end'][11:16]
    return bedtime_end
    
def get_readiness_score(date):
    readiness='https://api.ouraring.com/v1/readiness?start='+date+'&end='+date+'&access_token='+token
    with urllib.request.urlopen(readiness) as response:
        readiness = response.read()
    readiness=ast.literal_eval(readiness.decode())
    readiness_score=readiness['readiness'][0]['score']
    return str(readiness_score)

def get_movement(date):
    activity='https://api.ouraring.com/v1/activity?start='+date+'&end='+date+'&access_token='+token
    with urllib.request.urlopen(activity) as response:
        activity = response.read()
    activity=ast.literal_eval(activity.decode())
    movement=activity['activity'][0]['daily_movement']
    return str(movement)

def get_rest(date):
    activity='https://api.ouraring.com/v1/activity?start='+date+'&end='+date+'&access_token='+token
    with urllib.request.urlopen(activity) as response:
        activity = response.read()
    activity=ast.literal_eval(activity.decode())
    rest=activity['activity'][0]['rest']
    return str(rest)

def checkDate(date):
    try:
        tdatetime = dt.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


import tweepy
import time
# 上で取得した各種キーを入れる
CONSUMER_KEY = 'PpbxsZ0idtxs1TqvAFMGHClsu'
CONSUMER_SECRET = 'jcZxmw2Mk2csh0AGnuR6WE2BB7YdW6MysTAhxMON4qeUp6QCRE'
ACCESS_TOKEN = '4145420354-zbRBG6sNlDCE3FK8CkCHOrrXfD7SiidRmv4Okfi'
ACCESS_SECRET = '1WvMFmlmc4jAc3d35pGKlD7c0ktLETdJxeKHzIZMb3F85'
id_name='tubasasakunn'
action_name='bot'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#reply_list=[]


#APIインスタンスを作成

#while(True):
for i in range(1):
    #time.sleep(300)
    api = tweepy.API(auth)
    mention=api.mentions_timeline( count=20)
    tmaxtime = datetime.datetime.now()-datetime.timedelta(days=1)#dt.strptime('2020-09-20', '%Y-%m-%d')
    maxtime=tmaxtime.strftime("%Y-%m-%d")
    
    mintime='2020-06-01'
    tmintime=dt.strptime(mintime, '%Y-%m-%d')
    
    for status in mention:

        if status.text[len(id_name)+2:len(id_name)+2+len(action_name)]==action_name and not status.id in reply_list:
            reply_list.append(status.id)
        
            case=status.text[len(id_name)+2+len(action_name)+1:]#len(id_name)+2+len(action_name)+4]
            
            
            date=maxtime
            if 'date' in case:
                date=case[case.find('date')+5:case.find('date')+15]
                if not checkDate(date):
                    date=maxtime
                
                tdate = dt.strptime(date, '%Y-%m-%d')
                if tdate<tmintime or tdate>tmaxtime:
                    tdate=tmaxtime
                date=tdate.strftime("%Y-%m-%d")
            
            reply_text='@'+status.user.screen_name+' '
            
            if 'event' in case:
                reply_text=reply_text+get_event(date)
            
            elif 'age' in case:
                reply_text=reply_text+get_age()
                
            elif 'weight' in case:
                reply_text=reply_text+get_weight()+'kg'
                
            elif 'height' in case:
                reply_text=reply_text+get_height()+'cm'
                
            elif 'bedtime_start' in case:
                reply_text=reply_text+get_bedtime_start(date)
                
            elif 'bedtime_end' in case:
                reply_text=reply_text+get_bedtime_end(date)
            
            elif 'readiness' in case:
                tdate = dt.strptime(date, '%Y-%m-%d')-datetime.timedelta(days=1)
                date=tdate.strftime("%Y-%m-%d")
                reply_text=reply_text+get_readiness_score(date)+'%'
                tdate = dt.strptime(date, '%Y-%m-%d')+datetime.timedelta(days=1)
                date=tdate.strftime("%Y-%m-%d")
                
            elif 'movement' in case:
                reply_text=reply_text+get_movement(date)+'Meter'
            
            elif 'rest' in case:
                reply_text=str(reply_text)+get_rest(date)+'minute'

            elif 'poem' in case:
                reply_text=str(reply_text)+random.choice(poem_list)
        
            elif '詫び' in case:
                reply_text=str(reply_text)+random.choice(apology_list)
        
            elif '褒め' in case:
                reply_text=str(reply_text)+random.choice(praise_list)
        
            
        
            else:
                reply_text='@'+status.user.screen_name+'???'
                
            reply_text=reply_text+'\n'+date
            api.update_status(status = reply_text[:140], in_reply_to_status_id = status.id)

f = open(full_path+'reply_list.txt', 'w')
for x in reply_list:
    f.write(str(x) + "\n")
f.close()
