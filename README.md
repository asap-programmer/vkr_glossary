# Blockchain Glossary API

**Глоссарий терминов для исследования производительности различных блокчейн-платформ**

API для управления глоссарием терминов в рамках выпускной квалификационной работы по теме "Исследование производительности различных блокчейн-платформ".

## Описание проекта

Это RESTful API, построенное на FastAPI, предоставляющее полный функционал для управления глоссарием блокчейн-терминов:

- Создание, чтение, обновление и удаление терминов (CRUD операции)
- Валидация данных с помощью Pydantic
- Хранение данных в SQLite с использованием SQLAlchemy ORM
- Автоматическая миграция базы данных при старте
- Интерактивная документация API (Swagger UI и ReDoc)
- Статическая документация OpenAPI
- Полная контейнеризация с Docker и Docker Compose

## Технологический стек

- **FastAPI** - современный веб-фреймворк для создания API
- **Pydantic** - валидация данных и настройки
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - легковесная встраиваемая база данных
- **Docker & Docker Compose** - контейнеризация приложения
- **Uvicorn** - ASGI сервер

## Структура проекта

```
vkr_glossary/
├── app/
│   ├── __init__.py          # Инициализация пакета
│   ├── main.py              # Основное приложение FastAPI
│   ├── models.py            # SQLAlchemy модели БД
│   ├── schemas.py           # Pydantic схемы валидации
│   └── database.py          # Конфигурация базы данных
├── data/
│   └── glossary.db          # SQLite база данных (создается автоматически)
├── docs/
│   ├── openapi.json         # OpenAPI спецификация
│   ├── index.html           # Swagger UI документация
│   └── redoc.html           # ReDoc документация
├── Dockerfile               # Конфигурация Docker образа
├── docker-compose.yml       # Docker Compose конфигурация
├── requirements.txt         # Python зависимости
├── generate_docs.py         # Скрипт генерации статической документации
├── .gitignore              # Игнорируемые файлы Git
└── README.md               # Документация проекта
```

## API Endpoints

### Основные операции

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/` | Информация об API |
| GET | `/terms` | Получить все термины |
| GET | `/terms/{keyword}` | Получить термин по ключевому слову |
| POST | `/terms` | Создать новый термин |
| PUT | `/terms/{keyword}` | Обновить существующий термин |
| DELETE | `/terms/{keyword}` | Удалить термин |
| GET | `/categories` | Получить список категорий |
| GET | `/health` | Проверка работоспособности API |

### Примеры запросов

#### 1. Получение всех терминов

```bash
curl -X GET "http://localhost:8000/terms"
```

**Параметры запроса:**
- `skip` - количество пропускаемых записей (по умолчанию: 0)
- `limit` - максимальное количество записей (по умолчанию: 100)
- `category` - фильтр по категории (опционально)

**Пример с фильтром:**
```bash
curl -X GET "http://localhost:8000/terms?category=Основные%20понятия&limit=10"
```

#### 2. Получение конкретного термина

```bash
curl -X GET "http://localhost:8000/terms/Blockchain"
```

**Ответ:**
```json
{
  "id": 1,
  "keyword": "Blockchain",
  "definition": "Распределенная база данных, которая хранит информацию о транзакциях в виде цепочки блоков...",
  "category": "Основные понятия",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

#### 3. Создание нового термина

```bash
curl -X POST "http://localhost:8000/terms" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "DeFi",
    "definition": "Decentralized Finance - децентрализованные финансовые услуги на основе блокчейн технологий",
    "category": "Финансы"
  }'
```

#### 4. Обновление термина

```bash
curl -X PUT "http://localhost:8000/terms/DeFi" \
  -H "Content-Type: application/json" \
  -d '{
    "definition": "Decentralized Finance - экосистема финансовых приложений, построенных на блокчейне без посредников"
  }'
```

#### 5. Удаление термина

```bash
curl -X DELETE "http://localhost:8000/terms/DeFi"
```

## Установка и запуск

### Вариант 1: Запуск с Docker Compose (рекомендуется)

Это самый простой способ запуска приложения:

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/asap-programmer/vkr_glossary.git
cd vkr_glossary

# 2. Запустите приложение
docker-compose up --build
```

API будет доступен по адресу: `http://localhost:8000`

Документация: `http://localhost:8000/docs`

### Вариант 2: Запуск с Docker

```bash
# 1. Создайте Docker образ
docker build -t blockchain-glossary .

# 2. Запустите контейнер
docker run -d -p 8000:8000 -v $(pwd)/data:/app/data blockchain-glossary
```

### Вариант 3: Локальный запуск без Docker

```bash
# 1. Создайте виртуальное окружение
python -m venv venv

# 2. Активируйте виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите приложение
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Процесс развертывания

### Шаг 1: Подготовка окружения

Убедитесь, что у вас установлены:
- Docker (версия 20.10+)
- Docker Compose (версия 1.29+)

Проверка версий:
```bash
docker --version
docker-compose --version
```

### Шаг 2: Клонирование и настройка

```bash
# Клонируйте репозиторий
git clone https://github.com/asap-programmer/vkr_glossary.git
cd vkr_glossary

# Создайте директорию для данных
mkdir -p data
```

### Шаг 3: Сборка и запуск

```bash
# Сборка образа и запуск контейнера
docker-compose up --build -d

# Проверка статуса
docker-compose ps

# Просмотр логов
docker-compose logs -f
```

### Шаг 4: Проверка работоспособности

```bash
# Проверка health endpoint
curl http://localhost:8000/health

# Получение списка терминов
curl http://localhost:8000/terms

# Открытие документации в браузере
# Windows:
start http://localhost:8000/docs

# Linux/Mac:
open http://localhost:8000/docs
```

### Шаг 5: Остановка и очистка

```bash
# Остановка контейнеров
docker-compose down

# Остановка с удалением volumes
docker-compose down -v

# Полная очистка (образы, контейнеры, volumes)
docker-compose down --rmi all -v
```

## Интерактивная документация

FastAPI автоматически генерирует интерактивную документацию:

### Swagger UI
Доступна по адресу: `http://localhost:8000/docs`

Позволяет:
- Просматривать все доступные endpoints
- Тестировать API запросы прямо из браузера
- Просматривать схемы данных

### ReDoc
Доступна по адресу: `http://localhost:8000/redoc`

Альтернативная документация с улучшенным дизайном.

## Генерация статической документации

Для создания статической HTML документации:

```bash
# Убедитесь, что приложение может быть импортировано
python generate_docs.py
```

Это создаст директорию `docs/` с файлами:
- `openapi.json` - OpenAPI спецификация
- `index.html` - Swagger UI документация
- `redoc.html` - ReDoc документация

Эти файлы можно открыть в браузере без запущенного сервера.

## База данных

### Автоматическая миграция

При первом запуске приложение автоматически:
1. Создает директорию `data/`
2. Инициализирует SQLite базу данных `glossary.db`
3. Создает необходимые таблицы
4. Заполняет базу начальными терминами по блокчейну

### Структура таблицы `terms`

| Поле | Тип | Описание |
|------|-----|----------|
| id | INTEGER | Первичный ключ |
| keyword | VARCHAR(200) | Ключевое слово (уникальное) |
| definition | TEXT | Определение термина |
| category | VARCHAR(100) | Категория (опционально) |
| created_at | DATETIME | Дата создания |
| updated_at | DATETIME | Дата последнего обновления |

## Начальные данные

Приложение предзаполнено терминами по блокчейну:

- **Blockchain** - основное понятие распределенного реестра
- **Consensus** - механизмы консенсуса
- **Smart Contract** - умные контракты
- **Ethereum** - популярная блокчейн-платформа
- **Hyperledger Fabric** - корпоративная блокчейн-платформа
- **TPS** - транзакций в секунду
- **Latency** - задержка подтверждения
- **Gas** - плата за вычисления
- **Proof of Work** - алгоритм консенсуса
- **Proof of Stake** - энергоэффективный консенсус
- **Sharding** - метод масштабирования
- **Throughput** - пропускная способность

## Мониторинг и логирование

### Просмотр логов

```bash
# Логи всех сервисов
docker-compose logs -f

# Логи конкретного сервиса
docker-compose logs -f api

# Последние 100 строк
docker-compose logs --tail=100 api
```

### Health check

```bash
# Проверка через curl
curl http://localhost:8000/health

# Проверка Docker health status
docker-compose ps
```

## Валидация данных

Все входные данные валидируются с помощью Pydantic:

### Создание термина
- `keyword`: обязательное, 1-200 символов, не может быть пустым
- `definition`: обязательное, минимум 10 символов
- `category`: опциональное, максимум 100 символов

### Обновление термина
- `definition`: опциональное, минимум 10 символов если указано
- `category`: опциональное, максимум 100 символов


## Контакты

**Проект ВКР:** Исследование производительности различных блокчейн-платформ

**Репозиторий:** https://github.com/asap-programmer/vkr_glossary.git

## Заключение

Этот проект демонстрирует:
- ✅ Полный REST API с FastAPI
- ✅ Валидацию данных с Pydantic
- ✅ Работу с SQLite через SQLAlchemy
- ✅ Автоматическую миграцию БД
- ✅ Контейнеризацию с Docker
- ✅ Docker Compose для оркестрации
- ✅ Автоматическую документацию OpenAPI
- ✅ Статическую документацию
- ✅ Готовность к production deployment

Приложение готово к развертыванию и использованию для управления глоссарием терминов в рамках исследования блокчейн-платформ.
