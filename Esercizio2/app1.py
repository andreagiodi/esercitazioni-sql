from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql
import matplotlib.pyplot as plt
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    if request.args.get("radio") == 'radio1':
        query = 'SELECT category_name, count(*) as numero_prodotti FROM production.products inner join production.categories on categories.category_id = products.category_id GROUP BY category_name'
        df1 = pd.read_sql(query,conn)
        return render_template('result1.html', table = df1.to_html())
    elif request.args.get("radio") == 'radio2':
        query = 'SELECT sales.stores.store_name, count(*) as numero_ordini FROM sales.orders inner join sales.stores on sales.orders.store_id = sales.stores.store_id GROUP BY sales.orders.store_id, sales.stores.store_name'
        df2 = pd.read_sql(query,conn)
        return render_template('result2.html', table = df2.to_html())
    elif request.args.get("radio") == 'radio3':
        query = 'SELECT production.brands.brand_name, count(*) as numero_prodotti FROM production.products inner join production.brands on production.products.brand_id = production.brands.brand_id GROUP BY production.brands.brand_id, production.brands.brand_name'
        df3 = pd.read_sql(query,conn)
        return render_template('result3.html', table = df3.to_html())
    else:
        return render_template('result4.1.html')

@app.route('/result4', methods=['GET'])
def result4():
    NP = request.args.get("q")
    query = f"SELECT * FROM production.products where product_name LIKE '{NP}%' "
    df4 = pd.read_sql(query,conn)
    return render_template('result4.2.html', table = df4.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)