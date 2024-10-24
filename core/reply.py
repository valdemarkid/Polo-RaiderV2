import asyncio
import requests
from utils.init import *

async def replyspam():
    clear()
    logo()
    
    channelid = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Channel Id{ldb}]{lc} → ")
    msgid = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Message Id{ldb}]{lc} → ")
    msg = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Message{ldb}]{lc} ——→ ")
    with open('tokens.txt') as f:
        tokens = f.read().splitlines()

    def header(token, channelid, messageid, msg):
        payload = {
            'content': msg,
            'tts': False,
            'message_reference': {
                'channel_id': channelid,
                'message_id': messageid
            }
        }

        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        return payload, headers
    clear()
    logo()

    def sendmsg(token, channelid, msgid, msg):
        payload, headers = header(token, channelid, msgid, msg)

        response = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', json=payload, headers=headers)

        if response.status_code == 200:
            print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lg}Sent Succesfully")
        elif response.status_code == 429:
            print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lr}Rate Limited")
        else:
            print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")
            
    while True:
        for token in tokens:
            sendmsg(token, channelid, msgid, msg)