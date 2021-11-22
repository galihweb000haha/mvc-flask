import os
from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.models.gallery import Gallery
from app.models.testimoni import Testimoni
from app.models.user import User

@app.route('/', methods = ['GET'])
def index():
	user = User()
	gallery = Gallery()
	testimoni = Testimoni()
	data = {
			'user':user.get(),
			'gallery':gallery.get(),
			'testimoni':testimoni.get()
		}

	return render_template('index.html', data=data)

@app.route('/profile', methods = ['GET'])
def profile():
	user = User()
	data = user.get()
	return render_template('profile.html', data=data)
