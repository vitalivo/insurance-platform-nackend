#!/usr/bin/env bash
# Скрипт сборки для Render

set -o errexit  # Остановить выполнение при ошибке

echo "🚀 Начинаем сборку проекта..."

# Установка зависимостей
echo "📦 Установка зависимостей..."
pip install -r requirements.txt

# Сбор статических файлов
echo "📁 Сбор статических файлов..."
python manage.py collectstatic --noinput

# Применение миграций
echo "🗄️ Применение миграций..."
python manage.py migrate

# Создание суперпользователя
echo "👤 Создание суперпользователя..."
python manage.py create_superuser

echo "✅ Сборка завершена успешно!"