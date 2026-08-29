import allure
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage
from config import EMAIL, PASSWORD


@pytest.mark.ui
@allure.feature("Авторизация")
@allure.story("Вход в аккаунт")
@allure.title("Успешный вход в Yougile по email и паролю")
def test_login_positive(driver: WebDriver) -> None:
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу входа"):
        login_page.open()

    with allure.step("Выполнить вход с корректными данными"):
        login_page.login(EMAIL, PASSWORD)

    with allure.step("Проверить, что открылась страница со списком проектов"):
        projects_page = ProjectsPage(driver)
        add_project_link = projects_page.wait.until(
            EC.visibility_of_element_located(
                projects_page.ADD_PROJECT_LINK
            )
        )
        assert add_project_link.is_displayed()


@pytest.mark.ui
@allure.feature("Проекты")
@allure.story("Создание проекта")
@allure.title("Успешное создание проекта с задачами")
def test_create_project_positive(projects_page: ProjectsPage) -> None:
    title = "UI Autotest Project"

    with allure.step(f"Создать проект с названием '{title}'"):
        projects_page.create_project(title)

    with allure.step("Проверить, что открылась страница созданного проекта"):
        current_name = projects_page.get_current_project_name()
        assert title in current_name


@pytest.mark.ui
@allure.feature("Проекты")
@allure.story("Создание проекта")
@allure.title("Название созданного проекта совпадает с введённым")
def test_created_project_title_matches(
    projects_page: ProjectsPage,
) -> None:
    title = "UI Exact"

    with allure.step(f"Создать проект с названием '{title}'"):
        projects_page.create_project(title)

    with allure.step("Проверить точное совпадение названия проекта"):
        current_name = projects_page.get_current_project_name()
        assert title in current_name


@pytest.mark.ui
@allure.feature("Задачи")
@allure.story("Добавление задачи")
@allure.title("Успешное добавление задачи в проект")
def test_add_task_to_project_positive(
    projects_page: ProjectsPage,
) -> None:
    project_title = "UI Autotest Project For Task"
    task_title = "UI Autotest Task"

    with allure.step(f"Создать проект '{project_title}'"):
        projects_page.create_project(project_title)

    with allure.step(f"Добавить задачу '{task_title}'"):
        projects_page.add_task(task_title)

    with allure.step("Проверить, что задача появилась на доске"):
        tasks = projects_page.get_task_titles()
        assert task_title in tasks


@pytest.mark.ui
@allure.feature("Задачи")
@allure.story("Добавление задачи")
@allure.title("Последовательное добавление нескольких задач")
def test_add_multiple_tasks_positive(
    projects_page: ProjectsPage,
) -> None:
    project_title = "UI Autotest Multi Task Project"
    first_task = "First UI Task"
    second_task = "Second UI Task"

    with allure.step(f"Создать проект '{project_title}'"):
        projects_page.create_project(project_title)

    with allure.step("Добавить первую задачу"):
        projects_page.add_task(first_task)

    with allure.step("Добавить вторую задачу"):
        projects_page.add_task(second_task)

    with allure.step("Проверить, что обе задачи присутствуют на доске"):
        tasks = projects_page.get_task_titles()
        assert first_task in tasks
        assert second_task in tasks
