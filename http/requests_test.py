#coding=utf-8
import requests
# from pip._vendor.requests.auth import HTTPBasicAuth

# 多个参数格式：
# {"key1":"value1","key2":"value2","key3":"value3"}
yoyo_url='http://www.cnblogs.com/yoyoketang/'
blog_search_url='http://zzk.cnblogs.com/s/blogpost'

par={"Keywords":"youyouketang"}
r=requests.get(blog_search_url,params=par)

print r.text
r.status_code

# print (requests.get('http://localhost:8081/jenkins/api/json?pretty=true',auth=('admin','admin')).text)


# url='http://localhost:8081/jenkins/job/see_python_version/build'
# # r=requests.post(url,data={},auth=HTTPBasicAuth('admin','admin'))
# r=requests.post(url,data={},auth=('admin','admin'))
# print (r.status_code)
# print (r.headers)
# print (r.reason)