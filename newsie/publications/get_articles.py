from newsie.models import Article
import random
from .article_scraper import RssScraper

def update():

        urls = [
                'https://www.rte.ie/news/rss/news-headlines.xml',
                'https://www.independent.ie/breaking-news/rss/',
                'https://www.irishtimes.com/cmlink/news-1.1319192',
                'https://www.independent.ie/rss/'
        ]

        articles = []

        for url in urls:
                articles += RssScraper(url).articles

        return articles

