from bs4 import BeautifulSoup as bs
import urllib.request as req
import os
import time
#爬虫类
class reptile(object):
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }

    #创建并写入文件内容
    def writefile(self,file,data):
        f = open(file, "a", encoding='utf-8')
        f.write(data)
        f.close()

    #删除创建的文件
    def deletefile(self,file):
        if os.path.exists(file):
            os.remove(file)

    #打开网页
    def openurl(self,url):
        reqn = req.Request(url=url, headers=self.headers)
        soup = bs(req.urlopen(reqn), "html.parser")
        return soup

    #设置睡眠时间
    def sleep(self,s):
        time.sleep(s)
