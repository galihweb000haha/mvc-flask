import os
from flask import render_template, request, redirect, url_for, jsonify
from app import app
from app.models.gallery import Gallery
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.abspath('app/static/upload/gallery')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == "POST":
        file = request.files['foto']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gallery = Gallery()
            inputan = request.form
            message = gallery.store(filename, inputan['title'], inputan['content'])
            print(filename)
            data = gallery.get()
            return render_template('gallery.html', data=data)
    else :
        gallery = Gallery()
        data = gallery.get()
        return render_template('gallery.html', data=data)

@app.route('/gallery/getOne/<idx>', methods = ['GET'])
def getOne(idx=None):
    gallery = Gallery()
    data = gallery.getOne(idx)
    return jsonify(data)

@app.route('/gallery/destroy/<idx>', methods = ['GET'])
def destroy(idx=None):
    gallery = Gallery()
    data = gallery.delete(idx)
    
    data = gallery.get()
    return redirect('/gallery')

@app.route('/gallery/update/', methods = ['POST'])
def update():
    inputan = request.form
    gallery = Gallery()
    data = gallery.update(inputan['id'], inputan['title_ubah'], inputan['content_ubah'])
    
    data = gallery.get()
    return redirect('/gallery')
    