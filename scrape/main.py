from nyt_api import NYTApi
from write_output import write_to_json
from scrape import scrape_article
import pandas as pd

APIKEY = ""
URL = "https://www.cnn.com/2020/11/01/politics/election-2020-donald-trump-joe-biden-history/index.html"
PATH = "../data/articles/articles.json"

if __name__ == "__main__":
    # articles = NYTApi(APIKEY)
    # info = articles.request_info('election+ethnicity+president+US', 20)
    # write_to_json(PATH, info)

    article = scrape_article(URL, "CNN")
    data = pd.DataFrame.from_dict(article.__dict__)
    print(data)
    write_to_json(PATH, article.__dict__)