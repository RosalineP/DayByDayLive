
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, flash, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# SQL Handling -----------------------------------------------------------------------------------------------------------------------
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
    name = db.Column(db.String(50), primary_key=True)
    color = db.Column(db.String(50))
    userID = db.Column(db.String(4096))
    checked = db.Column(db.Boolean, default=False)

    def __init__(self, name, color, userID, checked):
        self.name = name
        self.color = color
        self.userID = userID
        self.checked = checked
# -------------------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def initialPage():
    userID = "user1" #login todo
    allCats = getCats(userID)
    return render_template('base.html', allCats=allCats)


def getCats(userID):
    return Categories.query.all()

@app.route('/addCat/', methods = ['POST'])
def addCat():
    #todo-login
    name = request.form['catName']
    color = request.form['catColor']

    if (not name) or (not color):
        return jsonify({"error":"Empty inputs!"})

    try:
        cat = Categories(name, color, "user1", False)
        db.session.add(cat)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Duplicate category!"})

    data = {"catName": name, "catColor": color}
    return jsonify(data)



