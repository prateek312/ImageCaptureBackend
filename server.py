#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import base64
import os.path
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def handle_request():
    try:
        request_data = request.get_json()
        decoded_data = base64.b64decode(request_data['imageData'])
        category_name = request_data['categoryName']
        image_name = str(int(time.time()))

        file_path = os.path.join(category_name, image_name + ".jpeg")

        img_file = open(file_path , 'wb')
        img_file.write(decoded_data)
        img_file.close()
        return ("Image Successfully")
    except: 
        return "Error while processing the request"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
