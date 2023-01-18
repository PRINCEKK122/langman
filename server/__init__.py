from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "eb48b9f8f7bb1916bea84e30692cc146"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///langman.db"
db = SQLAlchemy(app)
