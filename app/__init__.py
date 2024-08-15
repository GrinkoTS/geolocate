from flask import Flask
from config import my_key

app = Flask(__name__)
app.config['SECRET_KEY'] = my_key

from app import routes




