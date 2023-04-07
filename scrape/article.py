class Article:

    def __init__(self, source=""):
        self.headline = ""
        self.author = ""
        self.source = source
        self.published_date = {"month": "", "day": 0, "year": 0}
        self.article_content = ""
        self.url = ""

    def set_headline(self, headline):
        self.headline = headline.strip()


    def set_author(self, author):
        self.author = author.strip()
        

    def set_published_date(self, date):
        all_info = date.strip().split(" ")
        self.published_date["day"] = int(all_info[-2].strip(','))
        self.published_date["month"] = all_info[-3]
        self.published_date["year"] = int(all_info[-1])
        

    def set_content(self, raw_text_list):
        self.article_content = " ".join(raw_text_list)


    def set_url(self, url):
        self.url = url