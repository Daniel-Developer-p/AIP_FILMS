from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(127), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(70))
    title = db.Column(db.String(140), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref=db.backref('comments', lazy=True))


def find_by_text(text: str, articles):
    result = []
    text = text.lower()
    for article in articles:
        if text in article.title.lower() or text in article.body.lower():
            result.append(article)
    return result
