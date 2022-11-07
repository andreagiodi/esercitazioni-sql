from flask import Flask, render_template, request
import pandas as pd
import pymssql
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/ricerca", methods=["GET"])
def ricerca():
    nomeStore = request.args['negozio']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    query = f"SELECT sf.first_name, sf.last_name, st.store_name FROM sales.stores as st inner join sales.staffs as sf on st.store_id = sf.store_id where st.store_name = '{nomeStore}'"
    df = pd.read_sql(query,conn)
    if nomeStore not in df.store_name.to_list():
        return render_template("error.html")
                
    else:
        del df['store_name']
        return render_template("ricerca.html", nomiColonne = df.columns.values, dati = list(df.values.tolist()))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)