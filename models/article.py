# article_module.py
from db import db
import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(2), nullable=False)
    link = db.Column(db.String(255), nullable=False, unique=True)
    link_amp = db.Column(db.String(255), nullable=True)
    link_iframable = db.Column(db.Boolean, nullable=True)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    tags = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    hash = db.Column(db.String(10), nullable=False, unique=True)
    file = db.Column(db.String(255), nullable=True)
    permalink = db.Column(db.String(255), nullable=True)

    @classmethod
    def insert_from_feed(cls, source_id, feed_articles):
        stmt = Article.__table__.insert().prefix_with('IGNORE')
        articles = []
        for article in feed_articles:
            articles.append({
                'title': article['title'],
                'source': article['source'],  # Assuming 'source' is available in the feed
                'language': article.get('language', ''),  # Assuming 'language' is available in the feed
                'link': article['link'],
                'link_amp': article.get('link_amp', ''),
                'link_iframable': article.get('link_iframable', False),
                'time': datetime.datetime.utcnow(),
                'tags': article.get('tags', ''),
                'description': article.get('description', ''),
                'hash': article['hash'],  # Assuming 'hash' is available in the feed
                'file': article.get('file', ''),
                'permalink': article.get('permalink', ''),
            })
            db.engine.execute(stmt, articles)
            

        