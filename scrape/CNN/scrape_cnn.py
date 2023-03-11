from bs4 import BeautifulSoup
import sys
import json

sys.path.insert(0, "/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article
from write_output import write_to_json

PATH_WRITE = "../../data/articles/CNN/"

def scrape_cnn(url):

    soup = request_website(url)

    article = Article("CNN")
    article.set_url(url)

    ## get title headline
    try:
        article.set_headline(soup.find("h1", class_="headline__text inline-placeholder").text)
    except:
        print("Not article")
        return article

    ## get author
    try:
        article.set_author(soup.find("span", class_="byline__name").text)
    except:
        print("No Author")

    
    ## get date
    date = soup.find("div", class_="timestamp").text
    all_info = date.strip().split(" ")
    article.set_published_date(day=int(all_info[-2].strip(',')),
                               month=all_info[-3],
                               year=int(all_info[-1]))

    ## get text

    raw_text = soup.find("div", class_="article__content-container")
    if not raw_text:
        raw_text = soup.find("div", class_="article__content")
    
    try:
        content = raw_text.find_all("p")
        article.set_content([p.text.strip() for p in content])
    except:
        print("faulty article")
        return article
    return article


def get_links(year, main_bias):
    PATH = f"../../data/links/CNN/{main_bias}_{str(year)}.json"

    with open(PATH, 'r') as f:
        cur = json.loads(f.read())
        return cur
    

if __name__ == "__main__":

    MAIN_BIAS, YEAR = "immigration", 2021

    information = get_links(YEAR, MAIN_BIAS)
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    for url in information["Links"]:
        print(url)
        article = scrape_cnn(url)
        scrape_info["Articles"].append(article.__dict__)

    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)

