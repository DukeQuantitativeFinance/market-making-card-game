from mongoengine import Document, StringField, ListField

class Game(Document):
    game_id = StringField(primary_key=True)
    name = StringField(required=True)
    created_by = StringField(required=True)
    players = ListField(StringField())