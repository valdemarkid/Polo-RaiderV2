from utils.init import *

async def spammer():
    clear()
    logo()

    with open('tokens.txt') as f:
        tokens = f.read().splitlines()
    channelid = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Channel Id{ldb}]{lc} → ")
    messages = input(f"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Message{ldb}]{lc} → ")

    def spammer(token, channelid, messages):
        url = f'https://discord.com/api/v9/channels/{channelid}/messages'
        data = {"content": messages}
        headers = {"Authorization": token}
        while True: 
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lg}Sent Succesfully")
            else:
                print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")

    threads = []
    for token in tokens:
        thread = threading.Thread(target=spammer, args=(token, channelid, messages))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()