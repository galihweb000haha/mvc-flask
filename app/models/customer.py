from app import app
from app import mysql

class Customer:
	def get(self):
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM customers")
		return cursor.fetchall()
