import requests

import json

import datetime

import random

import string

import time

print ("2b1b5e4a-038f-49da-a69e-7882e8d59f8f")

print ("By - 6six6") 

referrer = input("WARP+ ID:otojepz117")

def genString(stringLength):

    letters = string.ascii_letters + string.digits

    return ''.join(random.choice(letters) for i in range(stringLength))

url = 'https://api.cloudflareclient.com/v0a745/reg'

def run():

    install_id = genString(11)

    body = {"key": "{}=".format(genString(42)),

            "install_id": install_id,

            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),

            "referrer": referrer,

            "warp_enabled": False,

            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",

            "type": "Android",

            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',

               'Host': 'api.cloudflareclient.com',

               'Connection': 'Keep-Alive',

               'Accept-Encoding': 'gzip',

               'User-Agent': 'okhttp/3.12.1'

               }

    r = requests.post(url, data=bodyString, headers=headers)

    return r

c = 1

while True:

    result = run()

    if result.status_code == 200:

        print(c,"GB added successfully!")

        c = c + 1

    else:

        time.sleep(1)

