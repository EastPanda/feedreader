from app import app
from db import db 
from models import articles
from models import source 

with app.app_context():
    db.create_all()

app.run()    