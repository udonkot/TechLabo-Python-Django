import requests

headers = {
    'Authorization': 'Bearer xoxb-83072119685-2963173195104-A52Wuo912tc1IeN9bBnPEBU2'
}


def get_reactions():
    url = 'https://slack.com/api/reactions.get'
    payload = {
        'channel': 'C03408J995K',
        'timestamp': '1670403607.218809',
        'pretty': '1'
    }
    res = requests.get(url=url, params=payload, headers=headers)
    res_json = res.json()
    return res_json


def get_users_list():
    url = 'https://slack.com/api/users.list'
    payload = {
        'pretty': '1'
    }
    res = requests.get(url=url, params=payload, headers=headers)
    res_json = res.json()
    return res_json
