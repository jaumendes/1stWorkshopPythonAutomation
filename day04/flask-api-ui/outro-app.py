from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="username",
    password="password",
    hostname="hostname",
    databasename="databsename",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

class Transactions1(db.Model):
     __tablename__ = "transactions1"

     trans_id = db.Column(db.Integer, primary_key=True)
     Item = db.Column(db.String(4096))
     Shack = db.Column(db.String(4096))
     Paym_Reference = db.Column(db.VARCHAR(20))
     Amount = db.Column(db.VARCHAR(10))


@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'GET':
        return render_template('Transactions.html')
    sale = Transactions1(Item=request.form["Item"],
                         Shack=request.form["Shack"],
                         Paym_Reference=request.form["Paym_Reference"],
                         Amount=request.form["Amount"])
    db.session.add(sale)
    db.session.commit()
    return render_template('Transactions.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
   
