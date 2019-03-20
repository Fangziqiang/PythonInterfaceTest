'''
Created on 2019年3月20日

@author: Administrator
'''
import requests
# from pip._vendor.requests.auth import HTTPBasicAuth

print (requests.get('http://localhost:8081/jenkins/api/json?pretty=true',auth=('admin','admin')).text)


url='http://localhost:8081/jenkins/job/see_python_version/build'
# r=requests.post(url,data={},auth=HTTPBasicAuth('admin','admin'))
r=requests.post(url,data={},auth=('admin','admin'))
print (r.status_code)
print (r.headers)
print (r.reason)