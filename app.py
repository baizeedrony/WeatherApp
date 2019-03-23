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
        'temperature' :,
        'description' :,
        'icon' :

    }
    return render_template('weather.html')

'''if __name__ ='__main__':
    run app'''
