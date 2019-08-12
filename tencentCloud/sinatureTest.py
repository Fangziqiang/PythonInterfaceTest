import hashlib
import base64
import hmac

secretKey = '2pM0PYR4SbT5cuxkMmxnO0NVO6ZnlYWL';
srcStr = 'GETapigateway.api.qcloud.com/v2/index.php?Action=DescribeApi&apiId=api-poopphj8&Nonce=12111&Region=bj&SecretId=AKIDsZ1RdekwEH5erqD4IH0ThsoUu4zeqFcl&serviceId=service-94vz3buz&SignatureMethod=HmacSHA256&Timestamp=1565591983';

srcStr = bytes("srcStr").encode('utf-8')
secretKey = bytes("secretKey").encode('utf-8')

signature = base64.b64encode(hmac.new(secretKey, srcStr, digestmod=hashlib.sha256).digest())

print(signature)
