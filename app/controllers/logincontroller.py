from flask import render_template, request, redirect
from app import app

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    return redirect('/')