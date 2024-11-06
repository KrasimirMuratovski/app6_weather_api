from flask import Flask, render_template, request

app = Flask("KM_Flask_One")

@app.route("/home/")
def home():
	return render_template("home.html")


@app.route("/about/")
def about():
	return render_template("about.html")

app.run(debug=True)
