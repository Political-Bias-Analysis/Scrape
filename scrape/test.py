import requests

APIKEY = "3T8SR9cP9qtApNkgsUxzBd0ne2vveGn5atgixQ4u"

def test():
    query = "cnn"
    date = "2020-11-01"
    try:
        a = requests.get(f"https://api.thenewsapi.com/v1/news/top?api_token={APIKEY}&search=usd&categories={query}")
        print(a.__dict__)
    except Exception as e:
        print(e)

test()