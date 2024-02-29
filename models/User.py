from mongoengine import Document, StringField

class User(Document):
    user_id = StringField(required=True)  # Define user_id as primary key
    username = StringField(required=True, max_length=50)
    password = StringField(required=True, max_length=100)
