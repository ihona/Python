import urllib
import urllib.request

request = urllib.request.Request('https://i.pximg.net/img-original/img/2017/05/24/17/08/22/63048381_p0.jpg')
response = urllib.request.urlopen(request)
get_img = response.read()
with open('D://text.jpg','wb') as f:
    f.write(get_img)
    print("ok")