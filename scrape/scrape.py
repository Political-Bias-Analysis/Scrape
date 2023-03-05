import requests
from bs4 import BeautifulSoup
from article import Article

def request_websites(url):

    link = requests.get(url).text
    soup = BeautifulSoup(link, 'lxml')
    return soup


def scrape_article(url, source):

    soup = request_websites(url)

    article = Article(source)

    ## get title headline
    article.set_title(soup.find("h1", class_="headline__text inline-placeholder").text)

    ## get author
    article.set_author(soup.find("span", class_="byline__name").text)

    ## get date
    article.set_published_date(soup.find("div", class_="timestamp").text)

    ## get text
    raw_text = soup.find("div", class_="article__content-container")
    content = raw_text.find_all("p")
    article.set_content([p.text.strip() for p in content])

    return article