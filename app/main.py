from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uvicorn

from app import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Blockchain Glossary API",
    description="API для управления глоссарием терминов исследования производительности блокчейн-платформ",
    version="1.0.0",
    contact={
        "name": "VKR Project",
        "url": "https://github.com/yourusername/vkr_glossary",
    },
    license_info={
        "name": "MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def startup_event():
    db = database.SessionLocal()
    try:
        existing_count = db.query(models.Term).count()
        if existing_count == 0:
            initial_terms = [
                {
                    "keyword": "Blockchain",
                    "definition": "Распределенная база данных, которая хранит информацию о транзакциях в виде цепочки блоков. Каждый блок содержит криптографическую хеш-функцию предыдущего блока, временную метку и данные транзакций.",
                    "category": "Основные понятия"
                },
                {
                    "keyword": "Consensus",
                    "definition": "Механизм достижения согласия между узлами распределенной сети относительно текущего состояния системы. Примеры: Proof of Work (PoW), Proof of Stake (PoS), Byzantine Fault Tolerance (BFT).",
                    "category": "Механизмы консенсуса"
                },
                {
                    "keyword": "Smart Contract",
                    "definition": "Программный код, который автоматически исполняется при выполнении определенных условий. Смарт-контракты хранятся и выполняются на блокчейне, обеспечивая прозрачность и неизменяемость.",
                    "category": "Технологии"
                },
                {
                    "keyword": "Ethereum",
                    "definition": "Децентрализованная платформа с открытым исходным кодом для создания смарт-контрактов и децентрализованных приложений (DApps). Использует собственную криптовалюту Ether (ETH).",
                    "category": "Платформы"
                },
                {
                    "keyword": "Hyperledger Fabric",
                    "definition": "Модульная блокчейн-платформа для корпоративного использования. Поддерживает приватные каналы, разрешенную сеть и гибкие механизмы консенсуса. Разработана Linux Foundation.",
                    "category": "Платформы"
                },
                {
                    "keyword": "TPS",
                    "definition": "Transactions Per Second - метрика производительности блокчейн-платформы, измеряющая количество транзакций, которые система может обработать за одну секунду.",
                    "category": "Метрики производительности"
                },
                {
                    "keyword": "Latency",
                    "definition": "Задержка - время, необходимое для подтверждения транзакции в блокчейн-сети. Важная метрика производительности, влияющая на пользовательский опыт.",
                    "category": "Метрики производительности"
                },
                {
                    "keyword": "Gas",
                    "definition": "Единица измерения вычислительных усилий, необходимых для выполнения операций в блокчейне Ethereum. Используется для оплаты комиссий за транзакции и выполнение смарт-контрактов.",
                    "category": "Экономика блокчейна"
                },
                {
                    "keyword": "Proof of Work",
                    "definition": "Алгоритм консенсуса, требующий от участников сети решения сложных криптографических задач для добавления новых блоков. Используется в Bitcoin, обеспечивает высокую безопасность, но энергоемкий.",
                    "category": "Механизмы консенсуса"
                },
                {
                    "keyword": "Proof of Stake",
                    "definition": "Алгоритм консенсуса, где право создания нового блока зависит от доли криптовалюты, которой владеет участник. Более энергоэффективен по сравнению с PoW.",
                    "category": "Механизмы консенсуса"
                },
                {
                    "keyword": "Sharding",
                    "definition": "Метод масштабирования блокчейна путем разделения сети на несколько подсетей (шардов), каждая из которых обрабатывает свою часть транзакций параллельно.",
                    "category": "Масштабирование"
                },
                {
                    "keyword": "Throughput",
                    "definition": "Пропускная способность - общее количество данных или транзакций, которое может быть обработано системой за определенный период времени.",
                    "category": "Метрики производительности"
                },
            ]

            for term_data in initial_terms:
                term = models.Term(**term_data)
                db.add(term)

            db.commit()
            print(f"✓ Инициализировано {len(initial_terms)} терминов в глоссарии")
        else:
            print(f"✓ База данных содержит {existing_count} терминов")
    finally:
        db.close()


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Blockchain Glossary API",
        "description": "API для управления глоссарием терминов исследования производительности блокчейн-платформ",
        "version": "1.0.0",
        "documentation": "/docs",
        "endpoints": {
            "GET /terms": "Получить список всех терминов",
            "GET /terms/{keyword}": "Получить термин по ключевому слову",
            "POST /terms": "Добавить новый термин",
            "PUT /terms/{keyword}": "Обновить существующий термин",
            "DELETE /terms/{keyword}": "Удалить термин"
        }
    }


@app.get("/terms", response_model=List[schemas.Term], tags=["Terms"])
async def get_all_terms(
    skip: int = 0,
    limit: int = 100,
    category: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(models.Term)

    if category:
        query = query.filter(models.Term.category == category)

    terms = query.offset(skip).limit(limit).all()
    return terms


@app.get("/terms/{keyword}", response_model=schemas.Term, tags=["Terms"])
async def get_term(keyword: str, db: Session = Depends(get_db)):

    term = db.query(models.Term).filter(
        models.Term.keyword.ilike(keyword)
    ).first()

    if term is None:
        raise HTTPException(
            status_code=404,
            detail=f"Термин '{keyword}' не найден в глоссарии"
        )

    return term


@app.post("/terms", response_model=schemas.Term, status_code=201, tags=["Terms"])
async def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    existing_term = db.query(models.Term).filter(
        models.Term.keyword.ilike(term.keyword)
    ).first()

    if existing_term:
        raise HTTPException(
            status_code=400,
            detail=f"Термин '{term.keyword}' уже существует в глоссарии"
        )

    db_term = models.Term(**term.model_dump())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)

    return db_term


@app.put("/terms/{keyword}", response_model=schemas.Term, tags=["Terms"])
async def update_term(
    keyword: str,
    term_update: schemas.TermUpdate,
    db: Session = Depends(get_db)
):

    db_term = db.query(models.Term).filter(
        models.Term.keyword.ilike(keyword)
    ).first()

    if db_term is None:
        raise HTTPException(
            status_code=404,
            detail=f"Термин '{keyword}' не найден в глоссарии"
        )

    # Обновляем только переданные поля
    update_data = term_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_term, field, value)

    db.commit()
    db.refresh(db_term)

    return db_term


@app.delete("/terms/{keyword}", tags=["Terms"])
async def delete_term(keyword: str, db: Session = Depends(get_db)):

    db_term = db.query(models.Term).filter(
        models.Term.keyword.ilike(keyword)
    ).first()

    if db_term is None:
        raise HTTPException(
            status_code=404,
            detail=f"Термин '{keyword}' не найден в глоссарии"
        )

    db.delete(db_term)
    db.commit()

    return {
        "message": f"Термин '{keyword}' успешно удален из глоссария",
        "deleted_term": db_term.keyword
    }


@app.get("/categories", tags=["Categories"])
async def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Term.category).distinct().all()
    return {
        "categories": [cat[0] for cat in categories if cat[0]]
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Проверка работоспособности API"""
    return {"status": "healthy", "service": "Blockchain Glossary API"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
