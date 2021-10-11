from app.main import db
from sqlalchemy import INTEGER, String, TIME
from sqlalchemy.schema import FetchedValue


class article(db.Model):
    __tablename__ = 'article'
    name = db.Column(String(), primary_key=True)  # Name | String
    content = db.Column(String())  # Content | String
    user = db.Column(String())  # User | String
    background = db.Column(String())  # Background | String
    customer = db.Column(INTEGER())  # Customer | String

    def __init__(self, name, content, user, background="White", customer=0):
        self.name = name
        self.customer = customer
        self.content = content
        self.user = user
        self.background = background

    def __repr__(self):
        return '<id {}>'.format(self.name)


class sign_up(db.Model):
    __tablename__ = 'sign_up'
    id = db.Column(INTEGER(), primary_key=True)  # ID | Integer
    username = db.Column(String(), unique=True)  # Username | String
    password = db.Column(String())  # Password | String

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class login(db.Model):
    __tablename__ = 'login'
    id = db.Column(INTEGER(), primary_key=True)  # ID | Integer
    username = db.Column(String())  # Username | String
    password = db.Column(String())  # Password | String

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(INTEGER(), primary_key=True)  # ID | Integer
    username = db.Column(String())  # Username | String
    customer = db.Column(INTEGER())  # Customer | Integer

    def __init__(self, username, customer):
        self.username = username
        self.customer = customer

    def __repr__(self):
        return '<id {}>'.format(self.id)
