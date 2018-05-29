#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def get_root():
    return "This is working !!!"


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=80, host='0.0.0.0')
