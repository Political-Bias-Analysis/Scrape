from bs4 import BeautifulSoup
import sys
import json

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article

from ReadWriteFiles.write_output import write_to_json
from ReadWriteFiles.read_write_links import get_links_by_year

PATH_WRITE = "../../data/articles/FOX/"

def scrape_fox(url):
    article = Article("FOX")
    article.set_url(url)
    soup = request_website(url)
    
    headline = soup.find("h1", class_="headline").text
    article.set_headline(headline)
    
    author_info = soup.find("div", class_="author-byline").text
    article.set_author(author_info)

    date = soup.find("time").text.strip()
    article.set_published_date(date)
    body = soup.find("div", class_='article-body')
    article.set_content([p.text.strip() for p in body.find_all("p")])
    return article


if __name__ == "__main__":

    MAIN_BIAS, YEAR = 'Racial', 2020
    MEDIA_NAME = "FOX"

    information = get_links_by_year(YEAR, MAIN_BIAS, MEDIA_NAME)
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    for url in information["Links"]:
        print(url)
        article = scrape_fox(url)
        scrape_info["Articles"].append(article.__dict__)
    
    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)