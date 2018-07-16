from reptile import reptile

datanum=1     #用于计数数据有多少条
data="" #用于存放临时数据
file = "Z:\python\爬虫\input.html" #指定将数据放到的页面
rep = reptile()
rep.deletefile(file)

#输入参数的25倍为具体爬到的数据数，因为豆瓣每25个数据为一个页面
for num in range(3):
    url = "https://" + "movie.douban.com/top250?start=" + str(num * 25)
    soup = rep.openurl(url)

    for link in soup.find_all("div", {"class": "item"}):
        href = str(link.contents[1].contents[1].find_next("a").get("href"))
        movename = str(link.contents[1].find_next("div").contents[1].find("span", {"class": "title"}).get_text())
        movenum = str(link.contents[1].find_next("div").contents[1].find_next("div").find("span",{"class": "rating_num"}).get_text())
        data = data+"<tr><td>" + str(datanum) + "</td><td><a href=" + href + " target=_blank>" + href + "</a></td><td>" + movename + "</td><td>" + movenum + "</td></tr>"

        datanum += 1
    rep.sleep(2)

data="<table>"+data+"</table>"
rep.writefile(file,data)