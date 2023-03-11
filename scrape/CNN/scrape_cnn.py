from bs4 import BeautifulSoup
import sys

sys.path.insert(0, "/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article

def scrape_cnn(url, source):

    soup = request_website(url)

    article = Article(source)

    ## get title headline
    article.set_headline(soup.find("h1", class_="headline__text inline-placeholder").text)

    ## get author
    article.set_author(soup.find("span", class_="byline__name").text)

    ## get date
    date = soup.find("div", class_="timestamp").text
    all_info = date.strip().split(" ")
    article.set_published_date(day=int(all_info[-2].strip(',')),
                               month=all_info[-3],
                               year=int(all_info[-1]))

    ## get text
    raw_text = soup.find("div", class_="article__content-container")
    content = raw_text.find_all("p")
    article.set_content([p.text.strip() for p in content])

    return article