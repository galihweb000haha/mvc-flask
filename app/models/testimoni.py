from app import app
from app import mysql

class Testimoni:
        def get(self):
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT customers.cust_id, customers.cust_name, testimoni.testimoni, testimoni.created_at FROM customers INNER JOIN testimoni ON testimoni.id_cust = customers.cust_id ")
                return cursor.fetchall()
        def store(self, foto, title, content):
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO testimoni VALUES (%s, %s, %s)", (foto, title, content))
                conn.commit()
                cursor.close()
                return true