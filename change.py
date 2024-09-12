import requests
import json
import time


def send_post_request():
    url = "https://fin.dding.net/v2/tenant/wechat/configure_password"
    headers = {
        "Host": "fin.dding.net",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.50(0x1800323d) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxb63528dc219b0805/26/page-frame.html",
    }

    data = {
        "userid": "",
        "token": "ea9dc69c-30a5-4808-b208-49621a0717f8",
        "gcid": "",
        "wechatId": "",
        "params": {
            "password": "923641",
            "compactId": "3EAC9E68A541DG4B95I8067G44B35F3021D7",
            "passwordId": "",
            "beginTime": "2024-09-01 00:00:00",
            "endTime": "2025-01-15 00:00:00",
            "uuid": "6f6f061aed68fea53e5f875a7699cf39",
        },
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 无限循环，每秒钟发送一次 POST 请求
while True:
    send_post_request()
    # time.sleep(1)
