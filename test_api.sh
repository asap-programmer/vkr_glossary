#!/bin/bash

# Скрипт для тестирования API
# Использование: ./test_api.sh

BASE_URL="http://localhost:8000"

echo "============================================"
echo "Тестирование Blockchain Glossary API"
echo "============================================"

echo -e "\n1. Проверка health endpoint"
echo "GET $BASE_URL/health"
curl -X GET "$BASE_URL/health"

echo -e "\n\n2. Получение информации об API"
echo "GET $BASE_URL/"
curl -X GET "$BASE_URL/"

echo -e "\n\n3. Получение всех терминов"
echo "GET $BASE_URL/terms"
curl -X GET "$BASE_URL/terms" | python -m json.tool | head -50

echo -e "\n\n4. Получение терминов по категории"
echo "GET $BASE_URL/terms?category=Основные понятия&limit=3"
curl -X GET "$BASE_URL/terms?category=Основные%20понятия&limit=3"

echo -e "\n\n5. Получение списка категорий"
echo "GET $BASE_URL/categories"
curl -X GET "$BASE_URL/categories"

echo -e "\n\n6. Получение конкретного термина"
echo "GET $BASE_URL/terms/Blockchain"
curl -X GET "$BASE_URL/terms/Blockchain"

echo -e "\n\n7. Создание нового термина"
echo "POST $BASE_URL/terms"
curl -X POST "$BASE_URL/terms" \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "NFT",
    "definition": "Non-Fungible Token - уникальный цифровой актив, представляющий право собственности на конкретный предмет или контент в блокчейне",
    "category": "Технологии"
  }'

echo -e "\n\n8. Получение созданного термина"
echo "GET $BASE_URL/terms/NFT"
curl -X GET "$BASE_URL/terms/NFT"

echo -e "\n\n9. Обновление термина"
echo "PUT $BASE_URL/terms/NFT"
curl -X PUT "$BASE_URL/terms/NFT" \
  -H "Content-Type: application/json" \
  -d '{
    "definition": "Non-Fungible Token - невзаимозаменяемый токен, криптографически уникальный цифровой актив на блокчейне",
    "category": "Цифровые активы"
  }'

echo -e "\n\n10. Проверка обновления"
echo "GET $BASE_URL/terms/NFT"
curl -X GET "$BASE_URL/terms/NFT"

echo -e "\n\n11. Удаление термина"
echo "DELETE $BASE_URL/terms/NFT"
curl -X DELETE "$BASE_URL/terms/NFT"

echo -e "\n\n12. Проверка удаления (должна вернуть 404)"
echo "GET $BASE_URL/terms/NFT"
curl -X GET "$BASE_URL/terms/NFT"

echo -e "\n\n============================================"
echo "Тестирование завершено!"
echo "============================================"
