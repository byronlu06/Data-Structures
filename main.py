from flask import render_template, request # flask
from flask import Blueprint
import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

dbURI = 'sqlite:///model/myDB.db'
db2 = 'sqlite:///model/myDB2.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SQLALCHEMY_DATABASE_2'] = db2
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


@app.route('/')
def index():
    return render_template("/home.html/")

@app.route('/byron/', methods=['GET', 'POST'])
def byron():

    url = "https://numbersapi.p.rapidapi.com/6/21/date"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "e919089b4amsh0b802c611d0362cp1ef95cjsn19265aeec315"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    mydict = json.loads(response.text)
    print(mydict)
    return render_template("/byron.html/", numbers=mydict)

if __name__ == "__main__":
    app.run(debug=True)
