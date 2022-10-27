from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    current_app
)
app = Flask(__name__)
import urllib.request 
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests,validators,json ,uuid,pathlib,os
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')



@app.route('/', methods=['GET'])
def home():
        
    return render_template('home.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)