# Python 3
import http.client, urllib.parse
import json

class Sources:
	def __init__(self,keyword):
		self.keyword=keyword;

	def extract(self,keyword):
		conn = http.client.HTTPConnection('api.mediastack.com')

		params = urllib.parse.urlencode({
		    'access_key': '0a1ef66a738531fe927dc81ea7cbc31d',
		    'categories': 'general,-sports',
		    'sort': 'published_desc',
		    'keywords':self.keyword,
		    'limit': 5,
		    })

		conn.request('GET', '/v1/news?{}'.format(params))

		res = conn.getresponse()
		data = res.read()
		# news = json.load(res)
		data = data.decode('utf-8')

		print(data[100])

		return data