import sqlite3
from flask import Flask
from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/result", methods=["POST"])
def result():
    kirja = request.form["kirja"]
    kirjailija = request.form["kirjailija"]
    tahti = request.form["tahti"]
    genres = request.form.getlist("genre")
    message = request.form["message"]
    return render_template("result.html", kirja=kirja, kirjailija=kirjailija, tahti=tahti, genres=genress, message=message)

