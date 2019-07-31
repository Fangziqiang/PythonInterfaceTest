#coding=utf-8
import requests
import json

# 对于https请求，直接发送请求会报错，可以加个参数，表示对SSL证书的验证
verify=False

orderlist_url="http://192.168.10.6:8080/owner/v1/orders/list"

headers ={"charset":"utf-8",
          "Accept-Encoding":"gzip",
          "authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJyYW5kb21LZXkiOiJyY3A1anIiLCJzdWIiOiIxMzI3MTU3MDUwMSIsImV4cCI6MTU2MjgyNDQ5MywiaWF0IjoxNTYyMjE5NjkzfQ.Z7KDpHMm9C16fR_5tQYZiL0_3XGOkZGnTSGsOwdzcZYeqSsCVG__-1zIRfCtRGoWLRy9LiqJRAc0XJyJZEB00A",
          "referer":"https://servicewechat.com/wxde3d576b9b28b080/0/page-frame.html",
          "hzcx-user":"ocYM-5S6uXbhThkPxxlaNaUdL0ek",
          "content-type":"application/json",
          "User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; MIX 2 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 MicroMessenger/7.0.4.1420(0x2700043C) Process/appbrand0 NetType/WIFI Language/zh_CN",
          "Host":"192.168.10.6:8080",
          "Connection":"Keep-Alive"
          }

payload = {"yoyo":"hello",u"python QQ群":"226296743"}


data_json=json.dumps(payload)
# post data格式
# r = requests.post("http://httpbin.org/post",data=payload)

# post json格式
r =requests.post("http://httpbin.org/post",json=data_json)

print (r.text)
