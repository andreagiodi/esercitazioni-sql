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
from urllib.request import urlopen
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')

url = "http://stadiumdb.com"


@app.route('/', methods=['GET'])
def home():
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<main>")
    start_index = title_index + len("<main>")
    end_index = html.find("</main>")
    title = html[start_index:end_index].replace("/img/", "http://stadiumdb.com/img/").replace("loading=\"lazy\"", "")
    return render_template('home.html', title=title)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)