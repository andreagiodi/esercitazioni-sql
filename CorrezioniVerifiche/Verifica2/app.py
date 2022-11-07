from flask import Flask, render_template, request
import pandas as pd
import pymssql
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/infoUser', methods=['GET'])
def infoUser():
    return render_template('info.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    nome = request.args['nome']
    cognome = request.args['cognome']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    query = f"SELECT * FROM sales.customers WHERE first_name = '{nome}' AND last_name = '{cognome}'"
    df = pd.read_sql(query,conn)
    if nome not in df.first_name.to_list() and cognome not in df.last_name.to_list():
        return render_template("error.html")
    else:
        print('ciao')
    return render_template('ricerca.html', nomiColonne = df.columns.values, dati = list(df.values.tolist()))



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)