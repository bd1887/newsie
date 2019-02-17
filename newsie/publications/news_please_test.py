from newsplease import NewscrawlerItem, NewsPlease


def news_plz():
    article = NewsPlease.from_url('https://www.independent.ie/sport/soccer/jurgen-klopp-charged-for-referee-comments-after-west-ham-game-37814103.html')
    return article