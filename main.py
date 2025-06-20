from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def load_country_data():
    with open('countries.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return {row['Country']: row for row in reader}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    country1 = request.form['country1']
    country2 = request.form['country2']

    data = load_country_data()

    if country1 not in data or country2 not in data:
        return "<h3>One or both countries not found in dataset.</h3><a href='/'>Try again</a>"

    c1 = data[country1]
    c2 = data[country2]

    return render_template('result.html', c1=c1, c2=c2)

if __name__ == '__main__':
    app.run(debug=True)
