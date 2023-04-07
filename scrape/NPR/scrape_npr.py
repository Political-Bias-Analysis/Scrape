from bs4 import BeautifulSoup
import sys
import json

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article

from ReadWriteFiles.read_write_links import get_links_by_year
from ReadWriteFiles.write_output import write_to_json

PATH_WRITE = "../../data/articles/NPR/"

def scrape_npr(url):
    article = Article("NPR")
    article.set_url(url)
    soup = request_website(url)
    
    headline = soup.find("div", class_="storytitle").text
    article.set_headline(headline)
    
    author_info = soup.find("div", class_="byline-container--block").text
    article.set_author(author_info)
    
    date = soup.find("span", class_="date").text.strip()
    article.set_published_date(date)
    
    ## Find normal text
    body1 = soup.find("div", id="storytext")
    text1 = [p.text.strip() for p in body1.find_all("p")]
    
    body2 = soup.find("div", class_="transcript storytext")
    text2 = []
    if body2:
        text2 = [p.text.strip() for p in body2.find_all("p")]
    article.set_content(text1 + text2)
    
    return article

if __name__ == "__main__":

    # item = scrape_npr("https://www.npr.org/2021/04/29/992097962/kris-kobach-former-trump-adviser-announces-run-for-kansas-attorney-general")
    # print(item.__dict__)
    MAIN_BIAS, YEAR = 'immigration', 2020
    MEDIA_NAME = "NPR"
    
    information = get_links_by_year(YEAR, MAIN_BIAS, MEDIA_NAME)
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    
    for url in information["Links"]:
        print(url)
        article = scrape_npr(url)
        scrape_info["Articles"].append(article.__dict__)
    
    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)