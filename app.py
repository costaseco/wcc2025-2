import requests
from flask import Flask, render_template, request

app = Flask(__name__)

cities = []

@app.route('/', methods=['GET'])
def index():
    city = 'Cascais'
    data = get_weather_by_location(city)
    return render_template('index.html', city=city, weather=data, cities=cities)

@app.route('/', methods=['POST'])
def index_post():
    city = request.form['city']
    cities.append(city)
    return index_by_city(city)

@app.route('/weather/<city>')
def index_by_city(city):
    data = get_weather_by_location(city)
    return render_template('index.html', city=city, weather=data, cities=cities)


def get_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=38.67&longitude=-9.32&current_weather=true&hourly=precipitation,cloudcover,winddirection_10m,apparent_temperature,temperature_2m,relativehumidity_2m,windspeed_10m'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data['hourly']

def get_location(city):
    headers = {
        "User-Agent": "SampleWeatherApp/1.0 (joao.seco@fct.unl.pt)"
    }

    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={city}&format=json", headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        lattitude = (float(data[0]['boundingbox'][0]) + float(data[0]['boundingbox'][1])) / 2
        longitude = (float(data[0]['boundingbox'][2]) + float(data[0]['boundingbox'][3])) / 2
        print(lattitude, longitude)
        return lattitude, longitude
    else:
        print(f"Error {response.status_code}: {response.text}")


def get_weather_by_location(city):
    lattitude, longitude = get_location(city)
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lattitude}&longitude={longitude}&current_weather=true&hourly=precipitation,cloudcover,winddirection_10m,apparent_temperature,temperature_2m,relativehumidity_2m,windspeed_10m'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data['hourly']

if __name__ == '__main__':
    app.run()
