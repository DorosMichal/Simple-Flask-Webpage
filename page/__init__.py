from flask import Flask
from flask_mysqldb import MySQL
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = MySQL(app)

from page import routes