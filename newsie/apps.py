from django.apps import AppConfig

class NewsieConfig(AppConfig):
    name = 'newsie'

    def ready(self):
        pass
        # self.update_articles()

    def update_articles(self):
        print("Updating articles...")
        from newsie.models import Article
        from newsie.publications import get_articles
        new_articles = get_articles.get_texts()
        for art in new_articles:
            db_art, created = Article.objects.get_or_create(url=art.url)
            
            db_art.title = art.title
            db_art.body = art.body
            db_art.description = art.description
            db_art.img = art.img
            db_art.pub_date = art.pub_date
            db_art.save()


    