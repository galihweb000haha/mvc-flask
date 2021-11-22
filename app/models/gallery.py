from app import app
from app import mysql

class Gallery:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gallery")
        return cursor.fetchall()

    def store(self, foto, title, content):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO gallery (foto, title, content) VALUES (%s, %s, %s)", ("gallery/"+foto, title, content))
        conn.commit()
        cursor.close()
        return "Berhasil"

    def getOne(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM gallery WHERE id_gallery ="+id)
        return cursor.fetchone()

    def delete(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM gallery WHERE id_gallery = "+id)
        conn.commit()
        cursor.close()
        return "Berhasil"

    def update(self, id, title, content):
        print("UPDATE FROM gallery SET title ='"+title+"', content = '"+content+"' WHERE id_gallery = "+id)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE gallery SET title ='"+title+"', content = '"+content+"' WHERE id_gallery = "+id)
        conn.commit()
        cursor.close()
        return "Berhasil"