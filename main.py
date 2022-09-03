import pandas as pd
from csv import writer
import csv
from flask import Flask, request, jsonify


df1= pd.read_csv('data.csv')
print(df1.to_json(orient='records'))

app = Flask(__name__)


@app.route('/')
def home():
    return "Home"


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
    return df1.to_json(orient='records')

if __name__ == "__main__":
    app.run(debug=True)
