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

SITE_BASE_URL нужно для префикса при создании URL. Он зависит от режима работы сервера, если DEBUG==True, то SITE_BASE_URL='http://127.0.0.1:8000/', иначе - значение берется из переменной окружения RAZZLE_SITE_BASE_URL

Другие необходимые переменные окружения:

`RAZZLE_DJANGO_SECRET_KEY` - необходимо сгенерировать случайный секретный ключ

`RAZZLE_DJANGO_DEBUG` - ненулевое значение делает DEBUG=False

`RAZZLE_EMAIL_HOST` - название почтового сервера, например, 'smtp.gmail.com'

`RAZZLE_EMAIL_PORT` - порт, например, у gmail - 587

`RAZZLE_EMAIL_HOST_USER` - почтовый ящик

`RAZZLE_EMAIL_HOST_PASSWORD` - пароль от почтового ящика

 `python manage.py runserver`


