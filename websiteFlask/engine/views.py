from engine import app
from flask import render_template, request, redirect, url_for, session


@app.route('/',methods=["POST","GET"])
def home():
    
    return render_template("home.html")

@app.route('/submit',methods=["POST","GET"])
def submit():
	if request.method == "POST":
		name = request.form["tudoubing"]
		print name
	return "Hello"

