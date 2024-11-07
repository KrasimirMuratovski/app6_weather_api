import pandas as pd
from flask import Flask, render_template

app=Flask(__name__)

df = pd.read_csv("dictionary.csv")
@app.route('/')
def home():
	return render_template('home_exer.html')

@app.route('/api/v1/<word>')
def api(word):
	output = df.loc[df['word'] == word]['definition'].squeeze()

	return {"definition": output,
			"word":word
			}

if __name__ == '__main__':
	app.run(debug=True, port=5001)
