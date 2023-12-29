from app import app
from db import db 
from models import article, source
from routes import route

with app.app_context():
    db.create_all()

app.run()    
