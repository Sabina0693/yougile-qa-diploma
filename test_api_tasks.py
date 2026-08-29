import allure
import pytest

from api.yougile_api import YougileApi


@pytest.mark.api
@allure.feature("Tasks API")
@allure.story("Создание задачи")
@allure.title("Успешное создание задачи в колонке")
def test_create_task_positive(
    api: YougileApi, column_id: str
) -> None:
    with allure.step("Отправить запрос на создание задачи"):
        resp = api.create_task(title="Autotest task", column_id=column_id)

    with allure.step("Проверить статус-код и наличие id в ответе"):
        assert resp.status_code == 201
        assert "id" in resp.json()


@pytest.mark.api
@allure.feature("Tasks API")
@allure.story("Создание задачи")
@allure.title("Создание задачи без обязательного поля title")
def test_create_task_negative_no_title(
    api: YougileApi, column_id: str
) -> None:
    with allure.step("Отправить запрос без поля title"):
        resp = api.create_task(title=None, column_id=column_id)

    with allure.step("Проверить статус-код и текст ошибки"):
        assert resp.status_code == 400
        assert "title should not be empty" in resp.json()["message"]


@pytest.mark.api
@allure.feature("Tasks API")
@allure.story("Получение задачи")
@allure.title("Успешное получение задачи по id")
def test_get_task_positive(
    api: YougileApi, column_id: str
) -> None:
    with allure.step("Создать задачу"):
        create_resp = api.create_task(
            title="Task to fetch", column_id=column_id
        )
        task_id = create_resp.json()["id"]

    with allure.step("Запросить задачу по id"):
        resp = api.get_task(task_id)

    with allure.step("Проверить статус-код и название задачи"):
        assert resp.status_code == 200
        assert resp.json()["title"] == "Task to fetch"
