from app import app
from flask_mysqldb import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'final_exam'

# Intialize MySQL
mysql = MySQL(app)