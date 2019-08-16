#coding=utf-8
import unittest
import requests
import json

# 登录页面
url1="https://passport.csdn.net/login"

# 登录请求
url2="https://passport.csdn.net/v1/register/pc/login/doLogin"

# 评论
url3="https://blog.csdn.net/u011541946/phoenix/comment/submit?id=77745924"

payload={"loginType":"1","pwdOrVerifyCode":"159753ai","userIdentification":"1174255033@qq.com","uaToken":"118#ZVWZzCEDIgirteKz8Z2CgZZTZebhreTVZZ2xojZhZHCzZgu/V5qVh+2zFBHhXHWpYg2Kus6TzHRzZJHZhoq1TZ2z8nHhXHRVZg4lZYqTaYQZZgZSTibSrdt8DYmGUH2ZZ1AuZkqhzeWzZZCCZw6SMbEmZeZTXHCwZg2ZusqTqCq2ZgZuTKq4ze2xxZChXHWVZgZZZsqTzeRzzZZZVoqVzHZZTHChXHWVZg2zVeghz+bp/y2gQKqWzpgZ/gwbXfRZ3SSgsmGjgrZZ4mG0jtAipj5JY6xWe7iEFhqoORrz3uPPqaPAOunzr6QNMx5oOUMKrDqsLKf9ugZCmrDtKHZzhS8V47UX9HZTlJIb2l6FwTGegrSTyi0wicJ+gLk/c2YIunDEl+P/iz3XkjA0mXSoR49fwUezEivkMZIpuVXSVpks9zmumGJjL9qdGT4SXJ4RCd3nzQpnsnKqbSKuFNNwlmQgkwFn3FIipsJIbGqPG/Pd8P0K3vVawbQacnKK1+rasPguVpFo4BR1Ypfydmydat6QG/KQMVzpcFp/9sboHm6/ifbE7TdhSwvETe1i6yFwOHlYFDC3wP+2v/ercb3mjZ6L+YrDQ+ukgRDAR+exhr6dYFh4evn2RoDhmtgpTPvD5Q0PVtxu+GDolvknTnqojnNDBz6ebHGV+JYxzRwioNYimlkgFFNKk2h+9JxURU7UFRqojeev3MqLv7Xrr+6nJFfRand7+X0xWDrNGm/bqw4dhcBVsxR6CH7MXMrHCA4D+catlfd1nuQzunZfGnGtPghvAW8zz+JfEho6Qxtsfdx7EUW+7QNeFtNjVQ+9ehxU+QM6FoutwPCm6YxewCMkMX0UEWxS3J/VymChQ/rmGxUVd5tTg5p+SWypqYypfptU0//02kffMKgzuKUu5rLciNTv8vWZSOlmjyLYZqNO54hP13UqmxdNNygg2Lhs+sX6U89rY0wnAVUz6uAO6W7f96Kshr1sOSiT90vJvJNt5pwEflyxkqtvJaEps8M/xydATAzQ8I3Asxd3i1nyIOuuR0g9xw9m9mxulBNZQsl+JA+Ka0G2kx/MYcpKXy1NPhJEZicJc9/Bz6T/8/W7WuBw0GNEjaZPRqTm/RrQ/A3LEeO3FqrDu+7HK33XXzDWOJ5T/RuabwfSssgctWObpGsblITKL9t89za3KWadY67LX5K/DKD4MRnAI2e3bN9SzPaia7rX0eqJ664fY8EP1KHiZY5twNIp0UYnPhA2Id5y+oakD+Xo1db2jpIZu4lpOUjse9GVVqQRgb3IgPG/UDlXE6iXsrDyKkyqikVSItHKzHEibnFFBeGOSOIkSM2ejYw/qT6uo2tfYMxxL4/X2qwbPHZuxzfn+37DSbPN3FhbiuKtPOiRl8PkDbKnJvjKTAayCM3LVaXE6Y5zaYhoR5bWQqXed+50P8m5aMcTgi4t0a4jafvCcJxTXeVMCNzpsDOcz5y/z1ZcSugz/+PyEJR/Z3cc5FCpwl/st0zonXN34TwR9cNWGvopQ8G5KbjscF/g+FDrAaybSC9+yEqPIBjoRyFXUUdC1fU12d04VGtcTVwl33pJ9deB99+1GO4uFKM+aiIxfjo15F0ogZtHWgyTLmj8fXjdx6jBg+PEqYR=","webUmidToken":"T640549AC072AF922B1FC4D7A1619482654FAE3C07E889CE1EB1B6DB229"}
d={"replyId":"","content":"很不错,赞一个"}

# data_json=json.dumps(payload)
# print data_json

# cookies绕过验证码登录：可以先手动登录一次，使用fiddler查看登录前后的cookies变化，然后向sessoin里添加登录成功后多出来的那些cookies
# 先打开登录首页，获取部分cookies
s=requests.session()
r_login=s.get(url1)
print s.cookies
print ("------------------------------------")

# 添加登录需要的cookies
c=requests.cookies.RequestsCookieJar()
c.set("UserName", "u010574553")
c.set("UserInfo", "50c096ebfdde4f288fb0720adb0b59cf")
c.set("UserToken", "50c096ebfdde4f288fb0720adb0b59cf")
c.set("UserNick", "ai30001")
c.set("AU", "D42")
c.set("UN", "u010574553")
c.set("BT","1565253969154")
c.set("p_uid", "U000000")
s.cookies.update(c)
print s.cookies
print ("-------------------------------------")

# 使用登录成功后的cookies免登录评论
comment_test=s.post(url3, data=d)
print comment_test.text



