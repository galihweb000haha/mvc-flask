from flask import render_template, request
from app import app
from app.models.testimoni import Testimoni

@app.route('/testimoni', methods=['GET', 'POST'])
def testimoni():
    if request.method == "POST":
        inputan = request.form
    else :
        testimoni = Testimoni()
        data = testimoni.get()
        return render_template('testimoni.html', data=data)