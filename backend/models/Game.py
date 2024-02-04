from flask_login import UserMixin
from mongoengine import Document, StringField, ListField, ReferenceField
    
from .User import User    
    
class Game(Document):
    game_id = StringField(max_length=100, unique=True)
    game_name = StringField(max_length=100)
    users = ListField(StringField())
    status = StringField(max_length=20)
    host = StringField(max_length=100)
