@echo off
REM Скрипт для локального запуска приложения на Windows
REM Использование: run_local.bat

echo Запуск Blockchain Glossary API локально...

REM Проверка наличия виртуального окружения
if not exist "venv\" (
    echo Создание виртуального окружения...
    python -m venv venv
)

REM Активация виртуального окружения
echo Активация виртуального окружения...
call venv\Scripts\activate.bat

REM Установка зависимостей
echo Установка зависимостей...
pip install -r requirements.txt

REM Создание директории для данных
if not exist "data\" mkdir data

REM Запуск приложения
echo.
echo Запуск приложения на http://localhost:8000
echo Документация доступна на http://localhost:8000/docs
echo Нажмите Ctrl+C для остановки
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
