# coding=utf-8
import urllib3
http=urllib3.PoolManager()
access_token = '24.745a2689abb8f19ffd58b5ede94ba6e6.2592000.1519880763.282335-10131029'
request=http.request('POST',
                        'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/static?access_token='+access_token
                    )
print(request.data)