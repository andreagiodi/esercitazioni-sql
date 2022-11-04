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


    if df[df['first_name'] == request.args['nome']]['first_name'].values[0]:
        if df[df['last_name'] == request.args['cognome']]['last_name'].values[0]:
            df1 = df[df['first_name'] == request.args['nome']]
        else:
            return render_template('error.html')    
    else:
        return render_template('error.html')

    #query1 = "SELECT * FROM Sales.customers WHERE first_name = " + request.args['nome'] + "AND WHERE last_name = " + request.args['last_name']
    #print(query)
    #df1 = pd.read_sql(query1,conn)


    return render_template('info.html', nomiColonne = df1.columns.values, dati = list(df1.values.tolist()), data = df1.to_html())




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)