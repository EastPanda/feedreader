from flask import Flask

app = Flask(__name__)

db_uri = 'postgresql://Islam:password@localhost:5432/feedparser'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri 