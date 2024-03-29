from bs4 import BeautifulSoup
import sys

sys.path.append("/Users/tramla/Desktop/UCI Courses/Senior-Project/Scrape/scrape/")
from scrape import request_website
from article import Article

from ReadWriteFiles.write_output import write_to_json
from ReadWriteFiles.read_write_links import get_links_by_year

PATH_WRITE = "/Users/tramla/Desktop/UCI Courses/Senior-Project/Data/data/articles/CBS/"

def scrape_cbs(url, bias):
    soup = request_website(url)
    
    
    article = Article("CBS", bias)
    article.set_url(url)
    
    
    article.set_headline(soup.find("h1", class_="content__title").text)
    
    try:
        byline = soup.find("p", class_="content__meta content__meta--byline").text
        article.set_author(get_author_name(byline))
    except:
        article.set_author("") 
    
    date = soup.find("time").text.split("/")[0]
    article.set_published_date(date)
        
    text_section = soup.find("section", class_="content__body")
    article.set_content([p.text for p in text_section.find_all("p")])

    return article

    
def get_author_name(byline):
    return " ".join(byline.strip().split(" ")[1:])
    
if __name__ == "__main__":
    
    MAIN_BIAS, YEAR = "socioeconomic", 2023
    MEDIA_SOURCE = "CBS"
    information = get_links_by_year(YEAR, MAIN_BIAS, MEDIA_SOURCE)
    
    scrape_info = {"Biases": information["Biases"], "Articles": []}
    for item in information["Links"]:
        print(item["link"])
        article = scrape_cbs(item["link"], item["bias"])
        if article:
            scrape_info["Articles"].append(article.__dict__)

    full_write_path = PATH_WRITE + MAIN_BIAS + '_' + str(YEAR) + '.json'
    write_to_json(full_write_path, scrape_info)