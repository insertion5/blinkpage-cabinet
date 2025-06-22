#!/bin/bash
# Настройка Django-проекта для деплоя на Render

echo "[1/4] Установка зависимостей..."
pip install -r requirements.txt

echo "[2/4] Применение миграций..."
python manage.py migrate

echo "[3/4] Создание суперпользователя..."
python manage.py createsuperuser

echo "[4/4] Готово! Запусти gunicorn с помощью Render или вручную:"
echo "gunicorn myproject.wsgi"
