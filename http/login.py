# coding=utf-8
import requests

login_url="http://192.168.10.6:8080/auth/login"
headers ={"charset":"utf-8",
          "Accept-Encoding":"gzip",
          "referer":"https://servicewechat.com/wxde3d576b9b28b080/0/page-frame.html",
          "hzcx-user":"ocYM-5S6uXbhThkPxxlaNaUdL0ek",
          "content-type":"application/json",# 如果post data数据，则这里使用 multipart/form-data
          "User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; MIX 2 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 MicroMessenger/7.0.4.1420(0x2700043C) Process/appbrand0 NetType/WIFI Language/zh_CN",
          "Host":"192.168.10.6:8080",
          "Connection":"Keep-Alive",
          }
# json格式
payload = {"phone":"17610831883","password":"111111"}
r = requests.post(login_url,json=payload,headers=headers,verify=False)

# post data格式 这个接口使用的是json格式
# d = {"phone":"17610831883","password":"111111"}
# r = requests.post(login_url,data=d,headers=headers,verify=False)


# r1=str(r.json())
# r2=r1.encode("raw_unicode_escape")
# r3=r2.decode()
print r.json(),u"结束","\n"
print r.text
# print r3