import pandas as pd
from csv import writer
from pandasql import sqldf
import csv
from flask import Flask, request, jsonify


df1= pd.read_csv('data.csv')
print(df1.to_json(orient='records'))
mysql = lambda q: sqldf(q, globals())

app = Flask(__name__)


@app.route('/')
def home():
    df2=mysql("SELECT * FROM df1 WHERE Name='ali';")
    return df2.to_json(orient='records')


@app.route("/predict", methods=['POST'])
def predict():
    name = request.form.get("name")
    maths = request.form.get("maths")
    sci = request.form.get("sci")
    List = [name,maths,sci]
    with open('data.csv', 'a', newline= '') as f_object:

        writer_object = writer(f_object)
        writer_object.writerow(List)

        f_object.close()
        df1 = pd.read_csv('data.csv')
    return df1.to_json(orient='records')

@app.route("/delete", methods=['POST'])
def d():
    name = str(request.form.get("name"))
    df1 = pd.read_csv('data.csv')
    df1= df1[df1.Name!=name]
    print(df1)
    df1.to_csv('data.csv',mode='w',index=False)
    df = pd.read_csv('data.csv')
    #return df1.to_json(orient='records')
    return mysql("SELECT * FROM data;")


if __name__ == "__main__":
    app.run(debug=True)
