from flask_login import UserMixin
from mongoengine import Document, StringField
    
class User(UserMixin, Document):
    user_id = StringField(max_length=100, unique=True)
    email = StringField(max_length=100, unique=True)
    password = StringField(max_length=255)