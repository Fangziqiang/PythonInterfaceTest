#coding=utf-8
import unittest
import requests
import json

url1="https://passport.csdn.net/login"
# 登录url
url2="https://passport.csdn.net/v1/register/pc/login/doLogin"
# CSDN博客发表评论url
url3="https://blog.csdn.net/u011541946/phoenix/comment/submit?id=77745924"

headers={"Host":"passport.csdn.net",
"Connection":"keep-alive",
"Content-Length":"1821",
"Accept":"application/json, text/plain, */*",
"Origin":"https://passport.csdn.net",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Content-Type":"application/json;charset=UTF-8",
"Referer":"https://passport.csdn.net/login",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9"
# "Cookie":"uuid_tt_dd=10_21002059980-1555919465131-685987; smidV2=20190416090651423004931c76eecf3477ef56da2cd6cc008cce21606d679b0; _ga=GA1.2.1175015664.1556268815; UN=u010574553; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_21002059980-1555919465131-685987!1788*1*PC_VC!5744*1*u010574553; dc_session_id=10_1557902436907.267433; UM_distinctid=16b870f94cb436-0faa2de70e13b8-454c092b-1fa400-16b870f94cc442; __guid=165585982.4398108816146534000.1563498443298.8755; BT=1563498768466; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1565140755,1565169389,1565169458,1565170233; aliyun_webUmidToken=T2BA0B4CEC705AC5875280BE63EC1FA6B8AAB808B504B478631A77E3243; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1565244201; c-login-auto=1; SESSION=21d3d4ac-9d01-459b-9bdc-a930583f3e50; monitor_count=2; dc_tos=pvwm6c"
}

payload={"loginType":"1","pwdOrVerifyCode":"159753ai","userIdentification":"1174255033@qq.com","uaToken":"118#ZVWZzCEDIgirteKz8Z2CgZZTZebhreTVZZ2xojZhZHCzZgu/V5qVh+2zFBHhXHWpYg2Kus6TzHRzZJHZhoq1TZ2z8nHhXHRVZg4lZYqTaYQZZgZSTibSrdt8DYmGUH2ZZ1AuZkqhzeWzZZCCZw6SMbEmZeZTXHCwZg2ZusqTqCq2ZgZuTKq4ze2xxZChXHWVZgZZZsqTzeRzzZZZVoqVzHZZTHChXHWVZg2zVeghz+bp/y2gQKqWzpgZ/gwbXfRZ3SSgsmGjgrZZ4mG0jtAipj5JY6xWe7iEFhqoORrz3uPPqaPAOunzr6QNMx5oOUMKrDqsLKf9ugZCmrDtKHZzhS8V47UX9HZTlJIb2l6FwTGegrSTyi0wicJ+gLk/c2YIunDEl+P/iz3XkjA0mXSoR49fwUezEivkMZIpuVXSVpks9zmumGJjL9qdGT4SXJ4RCd3nzQpnsnKqbSKuFNNwlmQgkwFn3FIipsJIbGqPG/Pd8P0K3vVawbQacnKK1+rasPguVpFo4BR1Ypfydmydat6QG/KQMVzpcFp/9sboHm6/ifbE7TdhSwvETe1i6yFwOHlYFDC3wP+2v/ercb3mjZ6L+YrDQ+ukgRDAR+exhr6dYFh4evn2RoDhmtgpTPvD5Q0PVtxu+GDolvknTnqojnNDBz6ebHGV+JYxzRwioNYimlkgFFNKk2h+9JxURU7UFRqojeev3MqLv7Xrr+6nJFfRand7+X0xWDrNGm/bqw4dhcBVsxR6CH7MXMrHCA4D+catlfd1nuQzunZfGnGtPghvAW8zz+JfEho6Qxtsfdx7EUW+7QNeFtNjVQ+9ehxU+QM6FoutwPCm6YxewCMkMX0UEWxS3J/VymChQ/rmGxUVd5tTg5p+SWypqYypfptU0//02kffMKgzuKUu5rLciNTv8vWZSOlmjyLYZqNO54hP13UqmxdNNygg2Lhs+sX6U89rY0wnAVUz6uAO6W7f96Kshr1sOSiT90vJvJNt5pwEflyxkqtvJaEps8M/xydATAzQ8I3Asxd3i1nyIOuuR0g9xw9m9mxulBNZQsl+JA+Ka0G2kx/MYcpKXy1NPhJEZicJc9/Bz6T/8/W7WuBw0GNEjaZPRqTm/RrQ/A3LEeO3FqrDu+7HK33XXzDWOJ5T/RuabwfSssgctWObpGsblITKL9t89za3KWadY67LX5K/DKD4MRnAI2e3bN9SzPaia7rX0eqJ664fY8EP1KHiZY5twNIp0UYnPhA2Id5y+oakD+Xo1db2jpIZu4lpOUjse9GVVqQRgb3IgPG/UDlXE6iXsrDyKkyqikVSItHKzHEibnFFBeGOSOIkSM2ejYw/qT6uo2tfYMxxL4/X2qwbPHZuxzfn+37DSbPN3FhbiuKtPOiRl8PkDbKnJvjKTAayCM3LVaXE6Y5zaYhoR5bWQqXed+50P8m5aMcTgi4t0a4jafvCcJxTXeVMCNzpsDOcz5y/z1ZcSugz/+PyEJR/Z3cc5FCpwl/st0zonXN34TwR9cNWGvopQ8G5KbjscF/g+FDrAaybSC9+yEqPIBjoRyFXUUdC1fU12d04VGtcTVwl33pJ9deB99+1GO4uFKM+aiIxfjo15F0ogZtHWgyTLmj8fXjdx6jBg+PEqYR=","webUmidToken":"T640549AC072AF922B1FC4D7A1619482654FAE3C07E889CE1EB1B6DB229"}
d={"replyId":"","content":"很不错,赞一个"}
# data_json=json.dumps(payload)
# print data_json
# 上一篇模拟登录博客园，但这只是第一步，一般登录后，还会有其它的操作，如发帖，评论等，这时候如何保持会话呢？
# 使用session保持会话
s=requests.session()
# 首先登录，将登录成功的会话会话信息保存为到session中
r=s.post(url2,json=payload)

# 使用预先保存的会话进行其他操作：这里进行评论操作
comment_test=s.post(url3, data=d)
# print r.content
# print r.text
print s.cookies
print comment_test.text