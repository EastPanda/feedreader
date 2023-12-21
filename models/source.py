import datetime
from db import db


class feed(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.Text, nullable = False)
    feed = db.Column(db.Text, nullable = False)
    title = db.Column(db.Text, nullable = False)
    subtitle = db.Column(db.Text, nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    

 