from bs4 import BeautifulSoup
import sys

sys.path.insert(0, "/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article
from write_output import write_to_json, add_to_json



PATH = "../../data/links/fox_links.txt"
PATH_WRITE = "../../data/articles/fox_articles.json"

def read_url():

    with open(PATH) as f:
        return [file.strip('\n') for file in f]

def scrape_fox(url):
    article = Article()
    soup = request_website(url)
    
    headline = soup.find("h1", class_="headline").text
    article.set_headline(headline)
    
    author_info = soup.find("div", class_="author-byline").text.strip()
    article.set_author(author_info)

    date = soup.find("time").text.strip()
    all_info = date.split(" ")
    article.set_published_date(month=all_info[0],
                               day=int(all_info[1].strip(',')),
                               year=int(all_info[2]))
    body = soup.find("div", class_='article-body')
    article.set_content([p.text.strip() for p in body.find_all("p")])
    return article



if __name__ == "__main__":
    urls = read_url()
    items = []
    for url in urls:
        article = scrape_fox(url)
        items.append(article.__dict__)

    write_to_json(PATH_WRITE, items)
