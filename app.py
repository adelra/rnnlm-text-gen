# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import os

app = Flask(__name__)



@app.route('/Result.html', methods=['POST'])
def summ():
	return none


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
