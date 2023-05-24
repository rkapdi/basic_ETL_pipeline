from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for
import requests
import pandas as pd
from ETL import generate_html_table, get_human_characters 

app = Flask(__name__)

@app.route('/')
def home():
    data = get_human_characters()
    return render_template('index.html', table=data)

@app.route('/get-data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        name = request.form.get('name')

        # Use the name to make a custom request to the API
        response = requests.get(f'https://rickandmortyapi.com/api/character/?name={name}')
        data = response.json()
        results = data.get('results', [])

        html_table = generate_html_table(results)
        return render_template('index.html', table=html_table)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
