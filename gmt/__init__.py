from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('gmt.config')

db = SQLAlchemy(app)

from gmt import views, models

db.create_all()
