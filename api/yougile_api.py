from typing import Optional

import requests


class YougileApi:
    """Клиент для работы с REST API Yougile."""

    def __init__(self, base_url: str, token: str) -> None:
        """
        Инициализирует клиента API.

        :param base_url: базовый адрес API, например
            "https://yougile.com/api-v2"
        :param token: токен авторизации (Bearer)
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    # ---------- Projects ----------

    def create_project(
        self, title: Optional[str] = None
    ) -> requests.Response:
        """
        Создаёт проект.

        :param title: название проекта (обязательное поле API)
        :return: объект ответа requests
        """
        body = {}
        if title is not None:
            body["title"] = title
        return requests.post(
            f"{self.base_url}/projects", json=body, headers=self.headers
        )

    def get_project(self, project_id: str) -> requests.Response:
        """
        Получает проект по ID.

        :param project_id: идентификатор проекта
        :return: объект ответа requests
        """
        return requests.get(
            f"{self.base_url}/projects/{project_id}", headers=self.headers
        )

    def update_project(
        self, project_id: str, title: Optional[str] = None
    ) -> requests.Response:
        """
        Обновляет проект.

        :param project_id: идентификатор проекта
        :param title: новое название проекта
        :return: объект ответа requests
        """
        body = {}
        if title is not None:
            body["title"] = title
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=body,
            headers=self.headers,
        )

    # ---------- Boards ----------

    def create_board(
        self, title: str, project_id: str
    ) -> requests.Response:
        """
        Создаёт доску внутри проекта.

        :param title: название доски
        :param project_id: идентификатор проекта-владельца
        :return: объект ответа requests
        """
        body = {"title": title, "projectId": project_id}
        return requests.post(
            f"{self.base_url}/boards", json=body, headers=self.headers
        )

    # ---------- Columns ----------

    def create_column(
        self, title: str, board_id: str
    ) -> requests.Response:
        """
        Создаёт колонку внутри доски.

        :param title: название колонки
        :param board_id: идентификатор доски-владельца
        :return: объект ответа requests
        """
        body = {"title": title, "boardId": board_id}
        return requests.post(
            f"{self.base_url}/columns", json=body, headers=self.headers
        )

    # ---------- Tasks ----------

    def create_task(
        self, title: Optional[str] = None, column_id: Optional[str] = None
    ) -> requests.Response:
        """
        Создаёт задачу в колонке.

        :param title: название задачи (обязательное поле API)
        :param column_id: идентификатор колонки (обязательное поле API)
        :return: объект ответа requests
        """
        body = {}
        if title is not None:
            body["title"] = title
        if column_id is not None:
            body["columnId"] = column_id
        return requests.post(
            f"{self.base_url}/tasks", json=body, headers=self.headers
        )

    def get_task(self, task_id: str) -> requests.Response:
        """
        Получает задачу по ID.

        :param task_id: идентификатор задачи
        :return: объект ответа requests
        """
        return requests.get(
            f"{self.base_url}/tasks/{task_id}", headers=self.headers
        )

    def update_task(
        self, task_id: str, title: Optional[str] = None
    ) -> requests.Response:
        """
        Обновляет задачу.

        :param task_id: идентификатор задачи
        :param title: новое название задачи
        :return: объект ответа requests
        """
        body = {}
        if title is not None:
            body["title"] = title
        return requests.put(
            f"{self.base_url}/tasks/{task_id}",
            json=body,
            headers=self.headers,
        )
