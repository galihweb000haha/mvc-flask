from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'poltek'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


from app.controllers import *
