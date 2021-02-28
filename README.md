создать и запустить виртуальное пространство:
`python -m venv env`

`cd env/Scripts`

`activate`

Сколнировать репозиторий: 
`https://github.com/BernarBerdikul/DRF_template.git`


Перейти в папку проекта:
`cd virtual_day`


Скачать все нужные библиотеки: 
`pip install -r requirements.txt`

Скопировать файл .env.example в ту же папку и переимновать в .env

Создать модель кэша 
`python manage.py createcachetable`

Создать БД в Postgresql (данные будут в файле .env.example), создать миграций и смигрировать туда данные:
`py manage.py makemigrations`
`py manage.py migrate`

Создать супер пользователя:
`py manage.py createsuperuser`

Запустить проект: 
`py manage.py runserver`
