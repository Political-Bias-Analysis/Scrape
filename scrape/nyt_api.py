import requests
import json

class NYTApi:
    def __init__(self, apikey):
        self.apikey = apikey


    def set_apikey(self, apikey):
        self.apikey = apikey

    def request_info(self, query, num_articles):
        pages = num_articles // 10
        all_info = []
        a = requests.get(f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q=new+york+times&page=2&sort=oldest&api-key={self.apikey}")
        for x in range(pages):
            try:
                response = requests.get(f'https://api.nytimes.com/svc/search/v2/articlesearch.json?\
                                        q={query}\
                                        &begin_date=20000101&end_date=20221231\
                                        &page={x}\
                                        &api-key={self.apikey}')
                info = response.json()
                for elem in info["response"]["docs"]:
                    cleaned_info = self.clean_data(elem)
                    all_info.append(cleaned_info)
            
            except Exception as e:
                print(e)
                print(info)
                break

        return all_info


    def clean_data(self, info):
        fields = {"abstract": "", "web_url": "", "headline": "", "keywords": [], "pub_date": ""}
        for field in fields:
            fields[field] = info[field]
        return fields
