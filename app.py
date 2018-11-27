
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, flash, request, redirect, url_for, session, jsonify


app = Flask(__name__)

@app.route('/')
def initialPage():
    return render_template('base.html')
