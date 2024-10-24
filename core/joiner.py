from utils.init import *
def get_tokens():
    try:
        with open('tokens.txt') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"                                          {ldb}[{s}!{ldb}] {s}| {r} Couldnt find tokens.txt, please make one manualy")
        return []
@dataclass
class JoinerData:
    pass
@dataclass
class Instance(JoinerData):
    client: requests.Session
    token: str
    invite: str
class Joiner:
    def __init__(self, data: Instance) -> None:
        self.session = data.client
        self.instance = data

    def join(self) -> None:
        self.session.headers.update({
            "Authorization": self.instance.token
        })
        result = self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}")
        if result.status_code == 200:
            print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {lg}Joined Succesfulley")
        else:
            print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")
class intilize:
    @staticmethod
    def start(i):
        Joiner(i).join()
async def tokenjoin():
    tokens = get_tokens()
    max_threads = 10  
    instances = []
    invite = input(f"[GLOO] | [INVITE] > discord.gg/")  
    for token in tokens:
        instances.append(Instance(
            client=requests.Session(),  
            token=token,
            invite=invite
        ))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(intilize.start, i) for i in instances]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"                                          {ldb}[{s}{crtime}{ldb}] {s}| {r} Failed")