import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = get_weather()
    return render_template('index.html', weather=data)

def get_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=38.67&longitude=-9.32&current_weather=true&hourly=precipitation,cloudcover,winddirection_10m,apparent_temperature,temperature_2m,relativehumidity_2m,windspeed_10m'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data['hourly']

if __name__ == '__main__':
    app.run()
