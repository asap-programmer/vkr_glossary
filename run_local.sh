#!/bin/bash

# Скрипт для локального запуска приложения без Docker
# Использование: ./run_local.sh

echo "Запуск Blockchain Glossary API локально..."

# Проверка наличия виртуального окружения
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate

# Установка зависимостей
echo "Установка зависимостей..."
pip install -r requirements.txt

# Создание директории для данных
mkdir -p data

# Запуск приложения
echo "Запуск приложения на http://localhost:8000"
echo "Документация доступна на http://localhost:8000/docs"
echo "Нажмите Ctrl+C для остановки"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
