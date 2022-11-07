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
import jsonify
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')

url = "https://footballgroundmap.com/news"


@app.route('/', methods=['GET'])
def home():
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<section class=\"pagecontainer\">>")
    start_index = title_index + len("<section class=\"pagecontainer\">>")
    end_index = html.find("</section>")
    title = html[start_index:end_index]##.replace("/img/", "http://stadiumdb.com/img/")
    return render_template('home.html', title=title)

@app.route('/test', methods=['GET'])
def test():
    query2 = "SELECT * FROM Stadio"
    df = pd.read_sql(query2,conn)
    return jsonify(df.to_json())

    #return render_template('test.html', value = df.to_json(orient='records')[1:-1].replace('},{', '} {')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)