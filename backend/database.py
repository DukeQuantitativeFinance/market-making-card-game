from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()
DB_URI = os.getenv('DB_URI')
db = connect("MarketMakingCardGame", host=DB_URI)
