from newsie.models import Article
import random
from .article_scraper import rss_scraper

def update():

        urls = {
                'Sports': [
                        'https://www.independent.ie/rss/sport/',
                        'https://www.rte.ie/rss/sport.xml',
                        'https://feeds.examiner.ie/iesport',
                ],
                'Business and Finance': [
                        'https://www.independent.ie/business/rss/',
                        'https://www.rte.ie/news/rss/business-headlines.xml',
                        'https://feeds.examiner.ie/iebusiness', 
                ],
                'Entertainment': [
                        'https://www.independent.ie/entertainment/rss/',
                ],
                'Health': [
                        'https://www.independent.ie/lifestyle/health/rss/',
                ],
                'Education': [
                        'https://www.independent.ie/lifestyle/education/rss/',
                ],
                'Life': [
                      'https://www.independent.ie/life/rss/',  
                ],
                'Travel': [
                        'https://www.independent.ie/life/travel/rss/',
                ],
                'Ireland': [
                        'https://www.independent.ie/irish-news/rss/',
                        'https://feeds.feedburner.com/ieireland',
                ],
                'World': [
                       'https://www.independent.ie/world-news/rss/',
                       'https://feeds.examiner.ie/ieworld', 
                ],
                'Unlabeled': [
                        'https://www.rte.ie/news/rss/news-headlines.xml',
                        'https://www.independent.ie/breaking-news/rss/',
                        'https://www.irishtimes.com/cmlink/news-1.1319192',
                        'https://www.independent.ie/rss/',   
                        'https://feeds.examiner.ie/ietopstories', 
                ],
                        
        }


        all_articles = []

        for key in urls:
                for url in urls[key]:
                        all_articles += rss_scraper(url, category=key)

        return all_articles

