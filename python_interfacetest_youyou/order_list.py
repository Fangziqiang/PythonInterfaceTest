#coding=utf-8

# coding=utf-8
import requests

order_list="http://192.168.10.6:8080/owner/v1/orders/list"
headers ={
          "charset": "utf-8",
          "Accept-Encoding": "gzip",
          "referer":"https://servicewechat.com/wx2ae551f4370691b6/0/page-frame.html",
          "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiJ5OWJtZTQiLCJzdWIiOiIxMzI3MTU3MDUwMSIsImV4cCI6MTU2NTc2NTIyMiwiZGV2aWNlSWQiOiIxMTUxNjc2MDA1MTA3MTA5ODg5MTU2MzQxNTkzMTg3N3RuayIsImlhdCI6MTU2NTE2MDQyMn0.Jx4nnrm_eZFYvtULgHmxxpRLCRzPlTxxDarDwnREMFWflrCssWS0mymQcesEiY8vo_Nh7T7cm4a-zN3gKo3U1A",
          "hzcx-user": "ofjzM4tJ7H_xUqgXZ0_27LFUMoRI",
          "content-type": "multipart/form-data",# 如果post data数据，则这里使用 multipart/form-dataapplication/json
          "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R9s Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand2 NetType/WIFI Language/zh_CN",
          "Host": "192.168.10.6:8080",
          "Connection": "Keep-Alive"
          }

# payload = {"phone":"17610831883","password":"111111"}
# get方法使用params参数
par={"status":"done","page":"0"}

# r = requests.get(order_list,headers=headers,data=d)
r = requests.get(order_list,headers=headers,params=par)

# r1=str(r.json())
# r2=r1.encode("raw_unicode_escape")
# r3=r2.decode()
print r.text
# print r3