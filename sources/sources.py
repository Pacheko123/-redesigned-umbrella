# Python 3
import http.client, urllib.parse
import json
import ast


class Sources:

    def extract(self, item):
        conn = http.client.HTTPConnection('api.mediastack.com')

        params = urllib.parse.urlencode({
            'access_key': '0a1ef66a738531fe927dc81ea7cbc31d',
            'categories': 'business,health,technology,science,health,general,sports',
            'sources': 'en,-de',
            'sort': 'published_desc',
            'keywords': item,
            'limit': 5,
        })

        conn.request('GET', '/v1/news?{}'.format(params))
        res = conn.getresponse()
        data1 = res.read()
        data = data1.decode('utf-8')
        news = json.loads(data)
        print(json.loads(data))

        try:
            news = news['data'][0]
            return news['author'], news['title'], news['description'], news['url'], news['source'], news['published_at']
        except:

            return news['author'], news['title'], news['description'], news['url'], news['source'], news['published_at']

        print(url)
        print(type(news))
