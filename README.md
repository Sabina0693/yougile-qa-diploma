# Yougile QA Automation — дипломный проект

Автоматизированные UI- и API-тесты для сервиса управления проектами
[Yougile](https://ru.yougile.com), реализованные в рамках дипломного
проекта на курсе Skypro «Инженер по тестированию ПО».

## Стек технологий

- Python 3.11+
- pytest — тест-раннер
- Selenium — UI-автотесты
- Requests — API-автотесты
- Allure — отчётность

## Структура проекта

```
.
├── api/
│   └── yougile_api.py       # API-клиент Yougile
├── pages/
│   ├── login_page.py        # PageObject: страница входа
│   └── projects_page.py     # PageObject: страница проектов
├── test_api_projects.py     # API-тесты: проекты
├── test_api_tasks.py        # API-тесты: задачи
├── test_ui_projects.py      # UI-тесты: вход, проекты, задачи
├── config.py                 # конфигурация (URL, токен, логин/пароль)
├── conftest.py                # фикстуры pytest
├── requirements.txt
└── README.md
```

## Установка

1. Клонировать репозиторий и перейти в его директорию.
2. Создать и активировать виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux/macOS
   .venv\Scripts\Activate.ps1    # Windows
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создать файл `local_settings.py` рядом с `config.py` со своими
   данными (файл не попадёт в git, он в `.gitignore`):
   ```python
   TOKEN = "твой_токен_yougile_api"
   EMAIL = "твой_email_для_входа"
   PASSWORD = "твой_пароль_для_входа"
   ```

## Запуск тестов

Только API-тесты:
```bash
pytest -m "api"
```

Только UI-тесты:
```bash
pytest -m "ui"
```

Все тесты:
```bash
pytest
```

## Формирование и просмотр отчёта Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Ссылка на тест-план и документацию проекта

<!-- вставить ссылку на страницу проекта в Yonote -->
