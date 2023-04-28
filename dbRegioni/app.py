from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pymssql



app = Flask(__name__)
conn = pymssql.connect(server='5.172.64.20', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')





@app.route('/', methods=['GET'])
def home():
    query = "SELECT * FROM Regioni"
    df = pd.read_sql(query,conn)
    return render_template('index.html', t=df)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)