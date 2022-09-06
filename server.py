#!/usr/bin/python
# -*- coding: utf-8 -*-
import flask
import requests
import werkzeug
import time

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
   imagefile = flask.request.files[0]
   filename = werkzeug.utils.secure_filename(imagefile.filename)
   print("Image Filename : " + imagefile.filename)
   timestr = time.strftime("%Y%m%d-%H%M%S")
   imagefile.save(timestr + '_' + filename)
   print("\n")
   return imageFile.filename

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
