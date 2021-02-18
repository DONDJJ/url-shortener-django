# url-shortener-django

# https://dondj-url.herokuapp.com/ - проект, развернутый на heroku

`git clone https://github.com/DONDJJ/url-shortener-django.git`

`cd url-shortener-django`

`pip install -r requirements.txt` - установка необходимых зависимостей

Создаем базу данных PostgreSQL с именем `url_shortener`

`python manage.py migrate` - применение необходимых миграций

В файле PetProject/settings.py изменяем

- ALLOWED_HOSTS=[] - для запуска на локальном сервере
- ALLOWED_HOSTS=[your-domain-name] 

SITE_BASE_URL нужно для префикса при создании URL
- SITE_BASE_URL='http://127.0.0.1:8000/' - для запуска на локальном сервере
- SITE_BASE_URL=protocol+domain-name

 `python manage.py runserver`
