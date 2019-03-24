import requests
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG']=True


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10'
    city = 'Las Vegas'
    r = requests.get(url.format(city)).json()
    print(r)
    weather = {
                  'city' :city,
                  'temperature' :r['main'] ['temp'],
                  'description' :r ['weather'][0]['description'],
                  'icon' :r ['weather'][0]['icon']

    }
    return render_template('weather.html')

if __name__ =='__main__':
    app.secret_key = 'super secret key'
    print(app.secret_key)
    app.run(debug=True)
