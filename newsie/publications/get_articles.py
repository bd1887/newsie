from newsie.models import Article
from newsie.publications.article_scraper import rss_scraper

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
                'https://www.rte.ie/news/rss/entertainment.xml',
                'https://feeds.breakingnews.ie/bnents?_ga=2.188804265.328186436.1557135717-1368852095.1557135717',
        ],
        'Health': [
                'https://www.independent.ie/lifestyle/health/rss/',
                'https://www.rte.ie/news/rss/health.xml'
        ],
        'Education': [
                'https://www.independent.ie/lifestyle/education/rss/',
                'https://www.rte.ie/news/rss/education.xml'
        ],
        'Ireland': [
                'https://www.independent.ie/irish-news/rss/',
                'https://www.rte.ie/news/rss/ireland.xml',
                'https://feeds.feedburner.com/ieireland',
        ],
        'World': [
                'https://www.independent.ie/world-news/rss/',
                'https://www.rte.ie/news/rss/world.xml',
                'https://feeds.examiner.ie/ieworld'
        ],
        'Unlabeled': [
                # 'https://www.rte.ie/news/rss/news-headlines.xml',
                # 'https://www.independent.ie/breaking-news/rss/',
                'https://www.irishtimes.com/cmlink/news-1.1319192',
                # 'https://www.independent.ie/rss/',   
                # 'https://feeds.examiner.ie/ietopstories', 
                'https://www.thejournal.ie/feed/',
        ],
}

# Scrape all articles in RSS feed url dictionary and preprocess
def update():
        all_articles = []
        for key in urls:
                for url in urls[key]:
                        #Returns a list of Article objects:
                        all_articles += rss_scraper(url, category=key)
        return all_articles

def categories():
        return [key for key in urls if key != 'Unlabeled']