#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import pytz
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def get_root():
    return "This is working !!!"


"""Get Server(North East Virginia) Time with Costa Rican time zone"""
@app.route('/server')
def server():
    try:
        tz = pytz.timezone('America/Costa_Rica')
        dt = datetime.now()
        loc_dt = tz.localize(dt).replace(microsecond=0)
        return str(loc_dt.isoformat())
    except Exception as e:
        print(e)
        return "Watch the logs."


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=80, host='0.0.0.0')
