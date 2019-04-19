from newsie.models import Article, ArticleCluster
from newsie.publications.get_articles import categories
from newsie.nlp.dbscan import dbscan

def merge_clusters():
    for category in categories():
        query_set = Article.objects.filter(category__exact=category)
        cluster_lists = dbscan(query_set)
        
        for cluster in cluster_lists:
            # Looks for lowest ArticleCluster id among articles in cluster if any exist
            lowest_db_cluster_id = min((article.cluster_id for article in cluster if article.cluster_id is not None), default=None)
            db_cluster = ArticleCluster.objects.get(pk=lowest_db_cluster_id) if lowest_db_cluster_id is not None else None

            # This is a new cluster:
            if db_cluster == None:
                # Create a new ArticleCluster object
                db_cluster = ArticleCluster.objects.create()

            # Assign this cluster as foreign key to each article
            for article in cluster:
                    article.cluster = db_cluster
                    article.save()

            # Update size, pub_date, category of cluster and saves
            db_cluster.update_metadata()