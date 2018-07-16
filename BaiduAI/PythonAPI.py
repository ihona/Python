# coding=utf-8
import urllib3, base64
import json

access_token = '24.745a2689abb8f19ffd58b5ede94ba6e6.2592000.1519880763.282335-10131029'
http = urllib3.PoolManager()
url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/static?access_token=' + access_token
f = open('D:/4_1.png', 'rb')

img = base64.b64encode(f.read())
params = {'image': '' + str(img, 'utf-8') + '', 'top_num': 5}
encoded_data = json.dumps(params).encode('utf-8')
print(encoded_data)
request = http.request('POST', url, body=encoded_data, headers={'Content-Type': 'application/json'})
result = str(request.data, 'utf-8')
print(result)
