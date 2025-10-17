# Quick Start Guide - Blockchain Glossary API

## Быстрый старт за 3 шага

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/yourusername/vkr_glossary.git
cd vkr_glossary
```

### 2️⃣ Запуск приложения

**Вариант A: Docker Compose (рекомендуется)**
```bash
docker-compose up --build
```

**Вариант B: Локально (Windows)**
```bash
run_local.bat
```

**Вариант C: Локально (Linux/Mac)**
```bash
chmod +x run_local.sh
./run_local.sh
```

### 3️⃣ Открыть документацию

Откройте в браузере: **http://localhost:8000/docs**

---

## Первые запросы

### Получить все термины
```bash
curl http://localhost:8000/terms
```

### Получить конкретный термин
```bash
curl http://localhost:8000/terms/Blockchain
```

### Создать новый термин
```bash
curl -X POST http://localhost:8000/terms \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "Web3",
    "definition": "Концепция децентрализованного интернета на основе блокчейн технологий",
    "category": "Технологии"
  }'
```

---

## Что включено

✅ **12 предзагруженных терминов** по блокчейну
✅ **Автоматическая документация** (Swagger UI + ReDoc)
✅ **SQLite база данных** с автоматической миграцией
✅ **Валидация данных** с Pydantic
✅ **Docker контейнеризация**
✅ **Полная CRUD функциональность**

---

## Полезные ссылки

| Ссылка | Описание |
|--------|----------|
| http://localhost:8000 | Главная страница API |
| http://localhost:8000/docs | Swagger UI документация |
| http://localhost:8000/redoc | ReDoc документация |
| http://localhost:8000/health | Health check |

---


## Остановка приложения

**Docker Compose:**
```bash
docker-compose down
```

**Локальный запуск:**
Нажмите `Ctrl+C` в терминале

---

## Помощь

**Проблемы?** Откройте issue на GitHub
**Вопросы?** Проверьте раздел "Решение проблем" в README.md

---

**Готово!** Теперь вы можете работать с API глоссария блокчейн-терминов! 🎉
