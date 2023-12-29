#app_module.py
from flask import Flask

app = Flask(__name__)

db_uri = 'postgresql://postgres:nomad@localhost:5432/feedreader'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri 
