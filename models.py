
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import datetime

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """user model for blogly. Include: id PK, first_name, last_name, image_url"""
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    species  = db.Column(db.String(50),
                        nullable=False,
                        unique=False)
    photo_url = db.Column(db.String(200),
                          nullable=True,
                          unique=False,
                          default="https://99designs-blog.imgix.net/blog/wp-content/uploads/2018/11/attachment_78456430-e1541654366936.jpeg?auto=format&q=60&fit=max&w=930")
    age = db.Column(db.Integer,
                    nullable=True)
    notes = db.Column(db.Text,
                      nullable=True)
    available = db.Column(db.Boolean,
                          default=True)
