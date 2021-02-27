#!/usr/bin/env python
# coding: utf-8


import numpy as np
import os


from flask import Flask, render_template
import pickle
import requests
import json
from flask import Response
from io import StringIO


application = Flask(__name__,template_folder='template')
@application.route('/')
def home():
    return render_template('index.html')
    

    



if __name__ == '__main__':
    application.run(debug=True)







