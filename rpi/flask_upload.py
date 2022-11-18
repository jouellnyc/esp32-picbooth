import os
from flask import Flask, flash, render_template, request
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = Flask(__name__)
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img/"
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        photos.save(request.files['photo'])
        flash("Photo saved successfully.")
        return render_template('upload.html')
    return render_template('upload.html')

@app.route("/picbooth/", methods=['GET'])
def picbooth():
    file='/root/picbooth/enc_text.txt'
    with open(file,'r') as fh:
        encoded=fh.read()
    return encoded


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


