from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def apis():
    params_1 = {
        'q': 'Minsk',
        'appid': 'bf9916088ad2517605a3912d42308578'
    }

    response_1 = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params_1)
    print(response_1.status_code)
    print(response_1.json())


    params_2 = {"currencies": "BYN",
                "source": "ARS",
                "apikey": "ftxI3cjCodPhbgauZkMey3RQdIs3Fibu"}

    response_2 = requests.get("https://api.apilayer.com/currency_data/live", params=params_2)
    return response_2.text

if __name__ == 'main':
    app.run()



