import allure
import pytest

from api.yougile_api import YougileApi


@pytest.mark.api
@allure.feature("Projects API")
@allure.story("Создание проекта")
@allure.title("Успешное создание проекта")
def test_create_project_positive(api: YougileApi) -> None:
    with allure.step("Отправить запрос на создание проекта"):
        resp = api.create_project(title="Autotest project")

    with allure.step("Проверить статус-код и наличие id в ответе"):
        assert resp.status_code == 201
        assert "id" in resp.json()


@pytest.mark.api
@allure.feature("Projects API")
@allure.story("Создание проекта")
@allure.title("Создание проекта без обязательного поля title")
def test_create_project_negative_no_title(api: YougileApi) -> None:
    with allure.step("Отправить запрос без поля title"):
        resp = api.create_project(title=None)

    with allure.step("Проверить, что сервер вернул ошибку 400"):
        assert resp.status_code == 400


@pytest.mark.api
@allure.feature("Projects API")
@allure.story("Получение проекта")
@allure.title("Успешное получение проекта по id")
def test_get_project_positive(
    api: YougileApi, project_id: str
) -> None:
    with allure.step("Запросить проект по id"):
        resp = api.get_project(project_id)

    with allure.step("Проверить статус-код и id проекта"):
        assert resp.status_code == 200
        assert resp.json()["id"] == project_id


@pytest.mark.api
@allure.feature("Projects API")
@allure.story("Обновление проекта")
@allure.title("Успешное обновление названия проекта")
def test_update_project_positive(
    api: YougileApi, project_id: str
) -> None:
    with allure.step("Отправить запрос на обновление названия"):
        resp = api.update_project(project_id, title="Updated title")

    with allure.step("Проверить статус-код обновления"):
        assert resp.status_code == 200

    with allure.step("Проверить, что название реально изменилось"):
        check = api.get_project(project_id)
        assert check.json()["title"] == "Updated title"
