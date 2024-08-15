from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import requests
from config import API_KEY, my_key

BASE_URL = 'http://suggestions.dadata.ru/suggestions/api/4_1/rs/geolocate/address'

app = Flask(__name__)
app.config['SECRET_KEY'] = my_key


@app.route('/', methods=('POST', 'GET'))
def index():
    """Обрабатывает главную страницу приложения. Принимает координаты широты
    и долготы (lat, lon) через POST-запрос. Использует API Dadata для поиска
    адреса по координатам. Если адрес найден, перенаправляет на страницу /address.
    В противном случае выводит сообщение об ошибке."""

    if request.method == 'POST':
        try:
            lat = float(request.form['lat'])
            lon = float(request.form['lon'])
            data = {
                'lat': lat,
                'lon': lon
            }
            url = BASE_URL
            headers = {
                "Content-type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Token {API_KEY}",
            }

            res = requests.post(url, data=json.dumps(data), headers=headers)
            sug = res.json()["suggestions"]
            if len(sug) != 0:
                address = sug[0]['unrestricted_value']
                first_address = address.split(',')
                session['first_address'] = first_address
                return redirect(url_for('address', _external=True), code=302)
            else:
                flash('Данный адрес не найден')
                raise 404
        except ValueError:
            flash('Введены неккоректные координаты')
            return redirect(url_for('index', _external=True), code=302)

    return render_template("geolocate.html")

@app.route('/address')
def address():
    """Обрабатывает страницу с адресом. Извлекает адрес из сессии.
    Если адрес найден -> отображает его на странице.
    В противном случае выводит сообщение об ошибке."""

    first_address = session.get('first_address', None)
    if first_address:
        return render_template('address.html', first_address=first_address)
    else:
        flash('Данный адрес не найден')
        raise 500


@app.errorhandler(404)
def pageNotFound(error):
    """Обрабатывает ошибку 404 (Страница не найдена)."""
    return render_template('page404.html', title='Страница не найдена')

@app.errorhandler(500)
def pageNotFound(error):
    """Обрабатывает ошибку 500 (Ошибка сервера)."""
    return render_template('page500.html', title='Ошибка сервера')



