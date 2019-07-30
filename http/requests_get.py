#coding=utf-8
import requests
# from pip._vendor.requests.auth import HTTPBasicAuth

# 多个参数格式：
# {"key1":"value1","key2":"value2","key3":"value3"}
yoyo_url='http://www.cnblogs.com/yoyoketang/'
blog_search_url='http://zzk.cnblogs.com/s/blogpost'
baidu_url='http://www.baidu.com'

par={"Keywords":"youyouketang"}

#请求博客搜索页
# r=requests.get(blog_search_url,params=par)

#请求百度首页
r=requests.get(baidu_url)

print r.url
print r.encoding    #编码格式
print r.content     #获取返回内容，这个方法会自动解码gzip和deflate压缩
print r.headers
print r.cookies
# response的其他返回内容
print r.status_code       #响应状态码
print r.raw               #返回原始响应体
print r.json()            #Requests中内置的JSON解码器
print r.raise_for_status()  #失败请求抛出异常（非200响应）

# print (requests.get('http://localhost:8081/jenkins/api/json?pretty=true',auth=('admin','admin')).text)


# url='http://localhost:8081/jenkins/job/see_python_version/build'
# # r=requests.post(url,data={},auth=HTTPBasicAuth('admin','admin'))
# r=requests.post(url,data={},auth=('admin','admin'))
# print (r.status_code)
# print (r.headers)
# print (r.reason)