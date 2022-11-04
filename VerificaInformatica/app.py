from flask import Flask, render_template, request
import pandas as pd
import pymssql
app = Flask(__name__)
conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')

@app.route('/infoUser', methods=['GET'])
def infoUser():
    return render_template('index.html')

@app.route('/info', methods=['GET'])
def info():
    query = 'SELECT * FROM Sales.Customers'
    df = pd.read_sql(query,conn)
    if request.args['nome'] == df.first_name:
        if request.args['cognome'] == df.last_name:
            df1 = df['first_name'] = request.args['nome'] and request.args['cognome']['']

    return render_template('info.html', nomiColonne = df1.columns.values, dati = list(df1.values.tolist()), data = df1.to_html())




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)