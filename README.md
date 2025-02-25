# Система управления заказами в кафе (Cafe Order System)

Это веб-приложение на Django для управления заказами в кафе. Оно позволяет добавлять, удалять, искать, изменять и отображать заказы, а также рассчитывать выручку за смену.

## Требования
- Python 3.8 или выше
- PostgreSQL 16.x или выше
- Django 4.0+
- djangorestframework 3.14+
- psycopg2-binary

## Установка

### 1. Клонирование проекта
Склонируйте репозиторий или создайте проект локально:
```bash
https://github.com/Rex-dev23/Coffe_Orders.git
cd Coffee_orders-
```
### 2. Создание проекта в PyCharm
Откройте PyCharm и выберите "Create New Project".
Выберите интерпретатор Python (рекомендуется Python 3.8+).
Нажмите "Create".
### 3. Инициализация Django проект
В PyCharm откройте терминал и выполните:
```bash
django-admin startproject cafe_order_system .
```
### 4. Создание приложения orders
В терминал PyCharm выполните:
```bash
python manage.py startapp orders\
```

### 5. Установка зависимостей
Убедитесь, что виртуальное окружение активировано автоматически в PyCharm.
Установите необходимые пакеты через терминал PyCharm:
```bash
pip install django psycopg2-binary djangorestframework
```
Создайте файл requirements.txt в корне проекта и добавьте:
```bash
Django>=4.0
psycopg2-binary>=2.9
djangorestframework>=3.14
```
### 6. Настройка Базы данных
Настройте settings.py в папке cafe_order_system
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cafe_orders_dbd',
        'USER': 'postgres',
        'PASSWORD': 'your_password',  # Замените на ваш пароль
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
    }
}
```
### Загрузите данные из бэкапа базы данных через графический интерфейс pgAdmin:
Откройте pgAdmin и подключитесь к серверу PostgreSQL.

В левой панели найдите базу данных cafe_orders_dbd.

Щелкните правой кнопкой мыши на базе cafe_orders_dbd и выберите "Restore" (Восстановить).
В диалоговом окне "Restore Database":

Нажмите на кнопку "..." рядом с полем "Filename" и выберите файл бэкапа cafe_orders_dbd.sql.

Убедитесь,что выбрано "Format: SQL Script".

Нажмите "Restore", чтобы загрузить данные из бэкапа в базу cafe_orders_dbd.

После завершения восстановления проверьте данные, щелкнув правой кнопкой мыши на таблицах (например, orders_order, orders_orderitem) и выбрав "View/Edit Data" → "All Rows".

### 7. Применение миграций
В PyCharm выполните в терминале:
```bash
python manage.py makemigrations
python manage.py migrate
```
### 8. Создание суперпользователя
Создайте пользователя для доступа к админ-панели:
```bash
python manage.py createsuperuser
```
### 9. Запуск приложения
Запустите сервер разработки в PyCharm через терминал:
```bash
python manage.py runserver
```
