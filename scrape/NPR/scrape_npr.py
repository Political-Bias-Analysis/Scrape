from bs4 import BeautifulSoup
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/scrape/")
from scrape import request_website
from article import Article

from ReadWriteFiles.read_write_links import get_links_by_year
from ReadWriteFiles.write_output import write_to_json

PATH_WRITE = "../../data/articles/NPR/"

def scrape_npr(url, bias):
    article = Article("NPR", bias)
    article.set_url(url)
    soup = request_website(url)
    
    try:
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
    except:
        print(f"Invalid article: {url}")
        return False
    
if __name__ == "__main__":

    MAIN_BIAS, YEAR = 'Abortion', 2014
    MEDIA_NAME = "NPR"
    
    information = get_links_by_year(YEAR, MAIN_BIAS, MEDIA_NAME)
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    
    for item in information["Links"]:
        #print(item["link"])
        article = scrape_npr(item["link"], item["bias"])
        if article:
            scrape_info["Articles"].append(article.__dict__)
    
    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)