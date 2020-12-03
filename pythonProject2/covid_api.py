from uk_covid19 import Cov19API
import json

config = open(r'C:\Users\adamg\PycharmProjects\pythonProject2\config.json', 'r')
config_json = json.load(config)

england_only = [
    'areaType=nation',
    'areaName=England'
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(filters=england_only, structure=cases_and_deaths, latest_by="newCasesByPublishDate")



json_data = api.get_json()
covid = json_data["data"]
print(covid)

covid_info = []
d={}
d['title'] = "Covid information"
d['content'] = covid
covid_info.append(d)
print(covid_info)
"""UK_covid_filepath = config_json['filepaths']['covid_json']
with open(r'{}'.format(UK_covid_filepath), 'w') as f:
    f.write(json_data)
    f.close()"""
