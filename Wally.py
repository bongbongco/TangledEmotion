#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from Crypto import Random
from Crypto.Cipher import AES
import base64

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! I'm Wally"

@app.route("/entered", methods=['GET'])
def enterdWallyWorld():
	error = None
    return "abcdefghijklmnopqrstuvwxyz123456"
	
if __name__ == "__main__":
    app.run()