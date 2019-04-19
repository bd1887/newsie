from newsie.models import Article
from newsie.nlp.tokenize import tokenize
from newsie.nlp.category_classifier import classify
from newsplease import NewsPlease
from bs4 import BeautifulSoup
from utils.strip_tags import strip_tags #Removes HTML tags
import datetime
from django.utils import timezone
import requests

def rss_scraper(rss_url, category):
    articles = []

    #If category is 'Unlabeled', then the article came from an unlabeled RSS feed
    # and won't be used for training the category classifier
    labeled = False if category == 'Unlabeled' else True

    resp = requests.get(rss_url) #GET request to RSS feed
    soup = BeautifulSoup(resp.content, "xml") #Parse
    items = soup.find_all("item") #Each <item> tag corresponds to one article

    for item in items:
        article_url = strip_tags(item.find_all("link")) #<link> tag holds the article url

        #Creates a NewsPlease object which automatically extracts information from article
        art = NewsPlease.from_url(article_url)

        ###NewsPlease attempts to extract the following information from the article: ###
        pub_date = datetime.datetime.combine(art.date_publish, datetime.time.min, timezone.utc)
        title = art.title
        description = art.description if art.description != None else ''
        body = art.text if art.text != None else ''
        img = art.image_url if art.image_url != None else ''
        ###

        article = Article(url=article_url, title=art.title, body=body, description=description, img=img, pub_date=pub_date, category=category, labeled=labeled)
        print(article.category, ' | ' ,article.title)
        articles.append(article)

    #Preprocesses, tokenizes, and gets trigrams from article text and saves it to Article object
    articles = tokenize(articles)

    #Attempts to predict the category of any unlabeled articles
    for article in articles:
        if article.category == 'Unlabeled':
            article.category = classify(article)

    return articles
