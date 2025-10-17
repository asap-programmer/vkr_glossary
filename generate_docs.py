"""
Скрипт для генерации статической документации OpenAPI
Использует встроенную спецификацию FastAPI для создания HTML документации
"""

import json
import os
from app.main import app


def generate_openapi_spec():
    """Генерация OpenAPI спецификации в JSON"""
    openapi_schema = app.openapi()

    # Создаем директорию для документации
    docs_dir = "docs"
    os.makedirs(docs_dir, exist_ok=True)

    # Сохраняем OpenAPI спецификацию
    spec_path = os.path.join(docs_dir, "openapi.json")
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump(openapi_schema, f, indent=2, ensure_ascii=False)

    print(f"✓ OpenAPI спецификация сохранена: {spec_path}")

    # Создаем HTML страницу с документацией Swagger UI
    swagger_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain Glossary API - Документация</title>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-standalone-preset.js"></script>
    <script>
        window.onload = function() {{
            window.ui = SwaggerUIBundle({{
                url: "openapi.json",
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIStandalonePreset
                ],
                plugins: [
                    SwaggerUIBundle.plugins.DownloadUrl
                ],
                layout: "StandaloneLayout"
            }})
        }}
    </script>
</body>
</html>"""

    swagger_path = os.path.join(docs_dir, "index.html")
    with open(swagger_path, "w", encoding="utf-8") as f:
        f.write(swagger_html)

    print(f"✓ Swagger UI документация сохранена: {swagger_path}")

    # Создаем ReDoc версию
    redoc_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain Glossary API - ReDoc</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body>
    <redoc spec-url="openapi.json"></redoc>
    <script src="https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js"></script>
</body>
</html>"""

    redoc_path = os.path.join(docs_dir, "redoc.html")
    with open(redoc_path, "w", encoding="utf-8") as f:
        f.write(redoc_html)

    print(f"✓ ReDoc документация сохранена: {redoc_path}")
    print("\nДокументация успешно сгенерирована!")
    print(f"Откройте {swagger_path} или {redoc_path} в браузере для просмотра.")


if __name__ == "__main__":
    generate_openapi_spec()
