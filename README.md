## Geolocate  
Представление интеграции для получения геолокационных данных с помощью API сервиса DaData.  
### Технологии  
Python3, Flask API
### Как запустить проект  

Клонировать репозиторий и перейти в него в командной строке:  
`git clone git@github.com:GrinkoTS/geolocate.git`  
`cd geolocate/`  

Создать и активировать виртуальное окружение:  
`python3 -m venv venv`  
`source venv/bin/activate`  
`python3 -m pip install --upgrade pip`  

Установить зависимости из файла requirements.txt:  
`pip install -r requirements.txt`  

В файле config.env прописываем свой токен с сайта DaData.

Запускаем приложение и в браузере прописываем url:  
`http://127.0.0.1:5001`



