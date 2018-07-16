from bs4 import BeautifulSoup
import requests
import json

movie_single = {}
for i in range(0, 10):
    res = requests.get('https://movie.douban.com/top250?start=' + str(i * 25) + '&filter=')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for movie in soup.select('.item'):
        movie_single['name'] = movie.select('a')[1].select('.title')[0].text
        movie_single['rating_num'] = movie.select('.rating_num')[0].text
        movie_single['director'] = movie.select('p')[0].contents[0].strip()
        movie_single['actor'] = movie.select('p')[0].contents[2].strip()
        try:
            movie_single['quote'] = movie.select('.inq')[0].text
            with open("D://top250.json", 'a', encoding='utf-8') as json_file:
                json.dumps(movie_single + '\n', json_file, ensure_ascii=False)
        except:
            pass
