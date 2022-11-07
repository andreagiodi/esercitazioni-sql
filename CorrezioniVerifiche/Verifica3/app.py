from flask import Flask, request, redirect, render_template
app = Flask(__name__)

import pandas as pd
import pymssql
import matplotlib.pyplot as plt

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/bestCustomers', methods=['GET'])
def bestCustomers():
    query = "SELECT top 10 sales.customers.customer_id, first_name, last_name, sum(list_price) as total_spent FROM sales.order_items inner join sales.orders on sales.order_items.order_id = sales.orders.order_id inner join sales.customers on sales.orders.customer_id = sales.customers.customer_id GROUP BY sales.customers.customer_id, sales.customers.first_name, sales.customers.last_name order by sum(list_price) desc"
    df = pd.read_sql(query,conn)
    return render_template('bestCustomers.html', nomiColonne = df.columns.values, dati = list(df.values.tolist()))

@app.route('/allOrders/<name>', methods=['GET'])
def allOrders(name):
    query2 = "SELECT * FROM sales.orders where sales.orders.customer_id = " + name
    df2 = pd.read_sql(query2,conn)
    return render_template('allOrders.html', nomiColonne = df2.columns.values, dati = list(df2.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)