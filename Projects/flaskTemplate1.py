#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:28:59 2018

@author: RoscoeBColtrane
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Exmaple of Flask db, 1.  CTRL + C will quit the local server."

app.run(port='8000')

