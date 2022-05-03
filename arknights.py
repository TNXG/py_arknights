from pathlib import Path
from arknight import Arknights, AkCall
import httpx
import json


def 干员id换名称(id):
    kkdyapi = 'https://test.api.kokodayo.fun/data/char?id='
    content = httpx.get(kkdyapi + id)
    json_str = json.loads(content.text)
    return json_str['result']['data']['name']


ark = Arknights(
    username="18888888888",                         # phone number
    password="xxxxxxx",                             # password
    access_token="",                                # access_token (if you have
    device_id="ffffffffffffffffffffffffffffffff",   # device_id
    device_id2="ffffffffffffffff",                  # device_id2
    relogin=False,                                  # auto relogin
    use_cache=True,                                 # use session cache
    session_dir=Path("accs"),                       # session_dir
    proxy="http://127.0.0.1:1080"                   # http proxy
)

ark.login()


user_data = AkCall.Account(ark).syncData()
print(f'现在这个大傻逼 {user_data["user"]["status"]["level"]} 级了')


search_player = AkCall.Social(ark).getSortListInfo("997437387", "")

player_list = AkCall.Social(ark).searchPlayer(
    [x["uid"] for x in search_player["result"]])


for players in player_list["players"]:
    nickName = str(players["nickName"])
    level = str(players["level"])
    charId = []
    for assistCharList in players["assistCharList"]:
        charId.append(assistCharList["charId"])
    charId1 = charId[0]
    charId2 = charId[1]
    charId3 = charId[2]

print('大佬的昵称：' + nickName + '；大佬的等级：' + level + '；助战干员是：' + 干员id换名称(charId1) + '，' + 干员id换名称(charId2) + '，' + 干员id换名称(charId3))
