import requests
import json

config = open('./config.json')
config_json = json.load(config)


base_url = "https://newsapi.org/v2/top-headlines?"
api_key = config_json["apikeys"]["news"]
country = "gb"
complete_url = base_url + "country=" + country + "&apiKey=" + api_key
# print response object
response = requests.get(complete_url)
news_dict = json.load(response)
articles = news_dict["articles"]
for article in articles:
		print(article['title'])