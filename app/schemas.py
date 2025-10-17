"""
Pydantic схемы для валидации данных
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class TermBase(BaseModel):
    """Базовая схема термина"""
    keyword: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Ключевое слово термина",
        examples=["Blockchain"]
    )
    definition: str = Field(
        ...,
        min_length=10,
        description="Определение термина",
        examples=["Распределенная база данных для хранения транзакций"]
    )
    category: Optional[str] = Field(
        None,
        max_length=100,
        description="Категория термина",
        examples=["Основные понятия"]
    )

    @field_validator('keyword')
    @classmethod
    def keyword_must_not_be_empty(cls, v: str) -> str:
        """Проверка, что ключевое слово не пустое"""
        if not v or not v.strip():
            raise ValueError('Ключевое слово не может быть пустым')
        return v.strip()

    @field_validator('definition')
    @classmethod
    def definition_must_not_be_empty(cls, v: str) -> str:
        """Проверка, что определение не пустое"""
        if not v or not v.strip():
            raise ValueError('Определение не может быть пустым')
        return v.strip()


class TermCreate(TermBase):
    """Схема для создания нового термина"""
    pass


class TermUpdate(BaseModel):
    """Схема для обновления термина"""
    definition: Optional[str] = Field(
        None,
        min_length=10,
        description="Новое определение термина"
    )
    category: Optional[str] = Field(
        None,
        max_length=100,
        description="Новая категория термина"
    )

    @field_validator('definition')
    @classmethod
    def definition_must_not_be_empty_if_provided(cls, v: Optional[str]) -> Optional[str]:
        """Проверка определения, если оно предоставлено"""
        if v is not None and (not v or not v.strip()):
            raise ValueError('Определение не может быть пустым')
        return v.strip() if v else v


class Term(TermBase):
    """Полная схема термина с метаданными"""
    id: int = Field(..., description="Уникальный идентификатор")
    created_at: Optional[datetime] = Field(None, description="Дата создания")
    updated_at: Optional[datetime] = Field(None, description="Дата последнего обновления")

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "id": 1,
                "keyword": "Blockchain",
                "definition": "Распределенная база данных, которая хранит информацию о транзакциях в виде цепочки блоков",
                "category": "Основные понятия",
                "created_at": "2024-01-15T10:30:00",
                "updated_at": "2024-01-15T10:30:00"
            }
        }
    }
