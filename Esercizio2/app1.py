from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    if request.args['a'] == 'numeroProdCat':
        return render_template('result.html')



@app.route('/test', methods=['GET'])
def test():
    import pandas as pd
    import pymssql
    import matplotlib.pyplot as plt
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea',                                        password='CarloCracco1962', database='giodice.andrea')
    nomeProdotto = request.args['NomeProdotto']
    query = f"SELECT * FROM production.products WHERE product_name LIKE '{nomeProdotto}%' "
    dfProdotti = pd.read_sql(query,conn)
    return render_template('result.html', nomiColonne = dfProdotti.columns.values, dati = list(dfProdotti.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)