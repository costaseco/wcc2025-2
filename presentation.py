from flask import Flask, render_template, request, json, make_response
from application import get_weather_in_city

# This module takes care of the connection to clients via a web application

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    cities = json.loads(request.cookies.get('cities', '[]'))
    if cities == []:
        cities = ['Cascais']
    city = cities[0]
    data, units = get_weather_in_city(city)
    response = make_response(render_template('index.html', city=city, units=units, weather=data, cities=cities))
    response.set_cookie('cities', json.dumps(cities, indent=4))
    return response

@app.route('/', methods=['POST'])
def index_post():
    cities = json.loads(request.cookies.get('cities', '[]'))
    city = request.form['city']
    cities.append(city)
    data, units = get_weather_in_city(city)
    response = make_response(render_template('index.html', city=city, units=units, weather=data, cities=cities))
    response.set_cookie('cities', json.dumps(cities, indent=4))
    return response

# presentation layer...
@app.route('/weather/<city>')
def index_by_city(city):
    cities = json.loads(request.cookies.get('cities', '[]'))
    data, units = get_weather_in_city(city)
    return render_template('index.html', city=city, units=units, weather=data, cities=cities)

if __name__ == '__main__':
    app.run()
