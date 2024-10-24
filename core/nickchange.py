from utils.init import *

def nicknamechange(token, guild_id, nickname):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/@me/nick"
    data = {
        "nick": nickname
    }
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lg}Changed")
    else:
        print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")
        
async def nickchange():
    with open('tokens.txt') as f:
        tokens = f.read().splitlines()

    guild_id = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}Server Id{ldb}]{lc} → ")
    nickname = input(fr"                                             {ldb}[{lc}Polo{ldb}] {s}| {ldb}[{lc}New Nickname{ldb}]{lc} → ")
    threads = []
    for token in tokens:
        thread = threading.Thread(target=nicknamechange, args=(token, guild_id, nickname))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
        
        time.sleep(2)
        clear()
        os.system('python polo.py')