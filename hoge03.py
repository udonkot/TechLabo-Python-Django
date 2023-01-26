import requests
import json
import datetime
import sys

# 基本設定
TOKEN = "xoxb-83072119685-2963173195104-A52Wuo912tc1IeN9bBnPEBU2"
url = "https://slack.com/api/conversations.history"
name_url = "https://slack.com/api/users.info"
header={
    "Authorization": "Bearer {}".format(TOKEN)
}

# 入力パラメータ
args = sys.argv
# print(sys.argv) # コマンド引数の配列取得
# print(len(sys.argv)) # 引数の数取得

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' 開始YYYYMMDD 終了YYYYMMDD')
    exit()

start_time_str = sys.argv[1]
end_time_str = sys.argv[2]

start_time = datetime.datetime.strptime(start_time_str, '%Y%m%d').timestamp()
end_time = datetime.datetime.strptime(end_time_str, '%Y%m%d').timestamp()

payload  = {
    "channel" : "C02D6RW3N83",
    "oldest" : str(start_time), #このタイムスタンプ以後の投稿が対象
    "latest" : str(end_time), #このタイムスタンプ以前の投稿が対象
    "limit" : "100000000000"
    }

res = requests.get(url, headers=header, params=payload)
json_data = res.json()
msg = json_data["messages"]

code_festa_dict = {}

for i in msg:
    if('reactions' in i):
        count = 0
        user = i["user"]

        payload = {
            "user" : user
            }

        res = requests.get(name_url, headers=header, params=payload)
        json_data = res.json()
        name = json_data["user"]["name"]

        for j in i["reactions"]:
            count += j["count"]

        if name in code_festa_dict:
            tmp = code_festa_dict[name]
            tmp += count
        else:
            code_festa_dict[name] = count

code_festa_dict = sorted(code_festa_dict.items(), key=lambda x: x[1], reverse=True)

[print(i) for i in code_festa_dict]
