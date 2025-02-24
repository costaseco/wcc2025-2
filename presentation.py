from flask import Flask, render_template, request
from application import add_city, cities, get_weather_in_city

# This module takes care of the connection to clients via a web application

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    city = 'Cascais'
    data = get_weather_in_city(city)
    return render_template('index.html', city=city, weather=data, cities=cities)

@app.route('/', methods=['POST'])
def index_post():
    city = request.form['city']
    add_city(city)
    return index_by_city(city)

# presentation layer...
@app.route('/weather/<city>')
def index_by_city(city):
    data = get_weather_in_city(city)
    return render_template('index.html', city=city, weather=data, cities=cities)

if __name__ == '__main__':
    app.run()
