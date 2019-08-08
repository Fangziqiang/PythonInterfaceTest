#coding=utf-8
import requests
import json

# 对于https请求，直接发送请求会报错，可以加个参数，表示对SSL证书的验证
verify=False

# post请求的参数可以放在url，也可以放在body，也可以同时放在url和body，也可以不带请求参数
# 一般来说，post请求的参数习惯放在body部分
# 常见的post提交数据类型有四种:
# 1.第一种：application/json  如：{"input1":"xxx","input2":"ooo","remember":false}
# 2.第二种：application/x-www-form-urlencoded：浏览器的原生 form 表单，如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数
# 3.第三种：multipart/form-data:这一种是表单格式的
# 4.第四种：text/xml:这种直接传的 xml 格式

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


# 将payload转换为json格式
data_json=json.dumps(payload)
# post data格式
# r = requests.post("http://httpbin.org/post",data=payload)

# post json格式
r =requests.post("http://httpbin.org/post",json=data_json)

print (r.text)
