import requests
from scrape import request_website
import json
from bs4 import BeautifulSoup

class NYTApi:

    PATH = "../data/links/election.json"

    def __init__(self, apikey):
        self.apikey = apikey


    def set_apikey(self, apikey):
        self.apikey = apikey

    def request_info(self, query, num_articles, start_date, end_date):
        pages = num_articles // 10
        all_info = []
        for x in range(pages):
            try:
                response = requests.get(f'https://api.nytimes.com/svc/search/v2/articlesearch.json?\
                                        q=politics\
                                        &fq=body:{query}\
                                        &begin_date={start_date}&end_date={end_date}\
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

    def get_article_links(self):
        get_file = open(NYTApi.PATH)
        article_info = json.load(get_file)
        return [article["web_url"] for article in article_info]


    def get_access(self, url):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} 
        response=requests.get(url, headers=headers) 
        print(response)
        soup = BeautifulSoup(response.content,'lxml') 
        for item in soup.select('.assetWrapper'): 
            try: 
                print('----------------------------------------') 
                headline = item.find('h2').get_text() 
                print(headline) 
            except Exception as e: 
                raise e 
            print('')

    def scrape_articles(self):
        links = self.get_article_links()
        for link in links:
            self.get_access(link)


    def archive(self, query, num_articles, start_date, end_date):
        response = requests.get(f'https://api.nytimes.com/svc/archive/v1/2019/1.json?&begin_date={start_date}&end_date={end_date}&api-key={self.apikey}')
        return response.json()["response"]["docs"]
