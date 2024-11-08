from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data-small/stations.txt", skiprows=17)
info = stations[['STAID', 'STANAME                                 ']]


@app.route("/")
def home():
	return render_template("home.html", data=info.to_html())


@app.route("/api/v1/<station>/<date>")  ## < > denotes user can enter value
def about(station, date):
	filename = 'data-small/TG_STAID' + str(station).zfill(6) + '.txt'
	df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
	temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
	return {"station": station,
			"date": date,
			"temperature": temperature}


app.run(debug=True, port=5000)

#
if '__name__' == '__main__':
	app.run(debug=True, port=5000)
