class Article:

    def __init__(self, source=""):
        self.headline = ""
        self.author = ""
        self.source = source
        self.published_date = {"month": "", "day": 0, "year": 0}
        self.article_content = ""

    def set_headline(self, headline):
        self.headline = headline.strip()


    def set_author(self, author):
        self.author = author


    def set_published_date(self, day, month, year):
        self.published_date["month"] = month
        self.published_date["day"] = day
        self.published_date["year"] = year


    def set_content(self, raw_text_list):
        self.article_content = " ".join(raw_text_list)

    