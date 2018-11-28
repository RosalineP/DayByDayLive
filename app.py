
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, flash, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# password may be pCkMY6aXKgW7geU
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="rosalinep",
    password="TBB5Hggi65DuYW3",
    hostname="rosalinep.mysql.pythonanywhere-services.com",
    databasename="rosalinep$DBD",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Categories(db.Model):
    __tablename__ = "category"
    # id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String(4096))
    name = db.Column(db.String(50), primary_key=True)
    color = db.Column(db.String(50))
    userID = db.Column(db.String(4096))


@app.route('/')
def initialPage():
    return render_template('base.html')


