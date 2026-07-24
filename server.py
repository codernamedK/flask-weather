# Main code file that will 

from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# Home page route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city', '')  # Get the city from the query parameters, default to empty string

    # checks for empty strings or string entered with only spaces, strip removes whitespace
    if not bool(city.strip()):
        city = "Richmond"

    weather_data = get_current_weather(city)

    # city is not found by the API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        'weather.html', 
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",   # formats to have extra .0 for temperature
        feels_like=f"{weather_data['main']['feels_like']:.1f}"  
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)


##@app.route('/weather', methods=['POST'])
##def weather():
##    city = request.form['city']
##    weather_data = get_current_weather(city)
##    return render_template('weather.html', weather=weather_data)