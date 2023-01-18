import enum
from server import db


class LanguageChoice(enum.Enum):
    en = "en"
    fr = "fr"
    es = "es"


class Usage(db.Model):
    __tablename__ = "usages"

    usage_id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.Enum(LanguageChoice))
    secret_word = db.Column(db.String(25), nullable=False)
    usage = db.Column(db.String(500), nullable=False)
    source = db.Column(db.String(100))
