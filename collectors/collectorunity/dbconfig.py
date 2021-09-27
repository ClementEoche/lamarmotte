from flask import Flask, MySQL
import configparser

app = Flask(__name__)
# Configuring Environment Variables
config = configparser.ConfigParser()
config.read('.env')
mysql = MySQL()

app.config['MYSQL_USER'] = config['local']['user']

app.config['MYSQL_PASSWORD'] = config['local']['password']

app.config['MYSQL_DB'] = config['local']['database']

app.config['MYSQL_CURSORCLASS'] = config['local']['cursor']

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_PORT'] = 3306

mysql.init_app(app)

def db_connection(): 
     try:
          cursor = mysql.connection.cursor()
     except Exception as error:
          raise error
     return cursor
