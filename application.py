import requests

# This module takes care of application logic, independent of the client applications.

# Orchestration of other services
def get_weather_in_city(city):
    latitude, longitude = get_location(city)
    return get_weather_by_location(latitude, longitude)

# Access to open-meteo service
def get_weather_by_location(lat, long):
    fields = 'precipitation,cloudcover,winddirection_10m,apparent_temperature,temperature_2m,relativehumidity_2m,windspeed_10m'
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true&hourly={fields}'
    response = requests.get(url)
    data = response.json()
    return data['hourly'], data['hourly_units']

# Access to openstreetmaps service
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



# Default implementation in the first try
def get_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=38.67&longitude=-9.32&current_weather=true&hourly=precipitation,cloudcover,winddirection_10m,apparent_temperature,temperature_2m,relativehumidity_2m,windspeed_10m'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data['hourly']

