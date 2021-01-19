import random
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp

app=Flask(__name__, static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/goodbye")
def bye():
    return "Goodbye!"

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.form.get('button'):
        number= random.randint(0,5)
        #number=5

        if number==0:
            return render_template("arms.html")
        elif number==1:
            return render_template("back.html")
        elif number==2:
            return render_template("chest.html")
        elif number==3:
            return render_template("legs.html")
        elif number==4:
            return render_template("sholders.html")
        elif number==5:
            return render_template("abs.html")
    return render_template("index.html")

@app.route("/leftarm", methods=["GET", "POST"])
def leftarm():
    if not request.form.get('left-arm'):
        return render_template("armworkout1.html")
    return render_template("arms.html")

@app.route("/rightarm", methods=["GET", "POST"])
def rightarm():
    if not request.form.get('right-arm'):
        return render_template("armworkout2.html")
    return render_template("arms.html")

@app.route("/armh", methods=["GET", "POST"])
def armhome():
    if not request.form.get('armhome'):
        return render_template("index.html")
    return render_template('arms.html')

@app.route("/leftback", methods=["GET", "POST"])
def leftback():
    if not request.form.get('left-back'):
        return render_template("backworkout1.html")
    return render_template("back.html")

@app.route("/rightback", methods=["GET", "POST"])
def rightback():
    if not request.form.get('right-back'):
        return render_template("backworkout2.html")
    return render_template("back.html")

@app.route("/backh", methods=["GET", "POST"])
def backhome():
    if not request.form.get('backhome'):
        return render_template("index.html")
    return render_template('back.html')

@app.route("/leftchest", methods=["GET", "POST"])
def leftchest():
    if not request.form.get('left-chest'):
        return render_template("chestworkout1.html")
    return render_template("chest.html")

@app.route("/rightchest", methods=["GET", "POST"])
def rightchest():
    if not request.form.get('right-chest'):
        return render_template("chestworkout2.html")
    return render_template("chest.html")

@app.route("/chesth", methods=["GET", "POST"])
def chesthome():
    if not request.form.get('chesthome'):
        return render_template("index.html")
    return render_template('chest.html')

@app.route("/leftleg", methods=["GET", "POST"])
def leftleg():
    if not request.form.get('left-leg'):
        return render_template("legworkout1.html")
    return render_template("leg.html")

@app.route("/rightleg", methods=["GET", "POST"])
def rightleg():
    if not request.form.get('right-leg'):
        return render_template("legworkout2.html")
    return render_template("leg.html")

@app.route("/legh", methods=["GET", "POST"])
def leghome():
    if not request.form.get('leghome'):
        return render_template("index.html")
    return render_template('legs.html')

@app.route("/leftsholder", methods=["GET", "POST"])
def leftsholder():
    if not request.form.get('left-sholder'):
        return render_template("sholderworkout1.html")
    return render_template("sholder.html")

@app.route("/rightsholder", methods=["GET", "POST"])
def rightsholder():
    if not request.form.get('right-sholder'):
        return render_template("sholderworkout2.html")
    return render_template("shodler.html")

@app.route("/shoulderh", methods=["GET", "POST"])
def shoulderhome():
    if not request.form.get('shoulderhome'):
        return render_template("index.html")
    return render_template('sholders.html')

@app.route("/leftabs", methods=["GET", "POST"])
def leftabs():
    if not request.form.get('left-abs'):
        return render_template("absworkout1.html")
    return render_template("abs.html")

@app.route("/rightabs", methods=["GET", "POST"])
def rightabs():
    if not request.form.get('right-abs'):
        return render_template("absworkout2.html")
    return render_template("abs.html")

@app.route("/absh", methods=["GET", "POST"])
def abshome():
    if not request.form.get('abshome'):
        return render_template("index.html")
    return render_template('abs.html')

@app.route("/home", methods=["GET", "POST"])
def home():
    if not request.form.get('Home'):
        return render_template("index.html")
    return redirect('/')







