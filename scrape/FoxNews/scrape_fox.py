from bs4 import BeautifulSoup
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/Scrape/scrape/")
from scrape import request_website
from article import Article

from ReadWriteFiles.write_output import write_to_json
from ReadWriteFiles.read_write_links import get_links_by_year

PATH_WRITE = "/Users/tramla/Desktop/UCI Courses/Senior-Project/data/articles/FOX/"

def scrape_fox(url, bias):
    article = Article("FOX", bias)
    article.set_url(url)
    soup = request_website(url)
    
    headline = soup.find("h1", class_="headline").text
    article.set_headline(headline)
    
    author_info = soup.find("div", class_="author-byline").text
    article.set_author(author_info)

    date = soup.find("time").text.strip()
    article.set_published_date(clean_date(date))
    body = soup.find("div", class_='article-body')
    article.set_content([p.text.strip() for p in body.find_all("p")])
    return article


def clean_date(date):
    return " ".join(date.split(" ")[:-2])


if __name__ == "__main__":

    MAIN_BIAS, YEAR = 'immigration', 2016
    MEDIA_NAME = "FOX"

    information = get_links_by_year(YEAR, MAIN_BIAS, MEDIA_NAME)
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    for item in information["Links"]:
        print(item["link"])
        article = scrape_fox(item["link"], item["bias"])
        scrape_info["Articles"].append(article.__dict__)
    
    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)