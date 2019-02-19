from newsie.models import Article
from newsplease import NewsPlease
from bs4 import BeautifulSoup
from .scraping_utils import strip_tags
import datetime
from django.utils import timezone
import requests

def rss_scraper(rss_url, category=''):
    articles = []
    category = category if category != 'Unlabeled' else ''

    resp = requests.get(rss_url)
    soup = BeautifulSoup(resp.content, "xml")
    items = soup.find_all("item")

    for item in items:
        article_url = strip_tags(item.find_all("link"))
        art = NewsPlease.from_url(article_url)
        pub_date = datetime.datetime.combine(art.date_publish, datetime.time.min, timezone.utc)
        description = art.description if art.description != None else ''
        body = art.text if art.text != None else ''
        img = art.image_url if art.image_url != None else ''

        article = Article(url=article_url, title=art.title, body=body, description=description, img=img, pub_date=pub_date, category=category)
        print(article.category, ' | ' ,article.title)
        articles.append(article)

    return articles