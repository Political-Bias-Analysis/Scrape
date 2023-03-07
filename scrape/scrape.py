import requests
from bs4 import BeautifulSoup
from article import Article

def request_website(url):

    link = requests.get(url).text
    soup = BeautifulSoup(link, 'lxml')
    return soup
