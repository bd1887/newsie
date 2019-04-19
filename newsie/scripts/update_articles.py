from newsie.models import Article
from newsie.publications.get_articles import update

def update_articles():
    new_articles = update()

    for art in new_articles:
        db_art, created = Article.objects.get_or_create(url=art.url)
        if created:
            db_art.title = art.title
            db_art.body = art.body
            db_art.description = art.description
            db_art.img = art.img
            db_art.pub_date = art.pub_date
            db_art.category = art.category
            db_art.tokens = art.tokens
            db_art.labeled = art.labeled
            db_art.save()