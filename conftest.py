from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from config import BASE_URL, TOKEN, EMAIL, PASSWORD
from api.yougile_api import YougileApi
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


def pytest_configure(config: "pytest.Config") -> None:
    """Регистрирует маркеры ui и api для запуска по режимам."""
    config.addinivalue_line("markers", "ui: UI-тесты (Selenium)")
    config.addinivalue_line("markers", "api: API-тесты (Requests)")


# ---------- API-фикстуры ----------

@pytest.fixture
def api() -> YougileApi:
    """Возвращает клиента API Yougile."""
    return YougileApi(BASE_URL, TOKEN)


@pytest.fixture
def project_id(api: YougileApi) -> Generator[str, None, None]:
    """Создаёт проект для теста и удаляет его после."""
    resp = api.create_project(title="Diploma test project")
    new_id = resp.json()["id"]

    yield new_id

    api.update_project(new_id, title="Diploma test project (archived)")


@pytest.fixture
def column_id(api: YougileApi, project_id: str) -> str:
    """Создаёт доску и колонку внутри проекта для тестов задач."""
    board_resp = api.create_board(
        title="Diploma test board", project_id=project_id
    )
    board_id = board_resp.json()["id"]

    column_resp = api.create_column(
        title="Diploma test column", board_id=board_id
    )
    return column_resp.json()["id"]


# ---------- UI-фикстуры ----------

@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Создаёт и завершает сессию веб-драйвера Chrome для UI-теста."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(5)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture
def projects_page(driver: WebDriver) -> ProjectsPage:
    """
    Выполняет вход в Yougile и возвращает готовую к работе
    страницу проектов.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(EMAIL, PASSWORD)

    return ProjectsPage(driver)
