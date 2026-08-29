from typing import List, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectsPage:
    """Страница списка проектов Yougile."""

    ADD_PROJECT_LINK = (
        By.XPATH, "//span[contains(text(),'Добавить проект')]"
    )
    ADD_PROJECT_CARD = (
        By.CSS_SELECTOR, "[data-testid='add-project-card']"
    )
    PROJECT_WITH_TASKS_OPTION = (
        By.CSS_SELECTOR,
        "[data-testid='menu-item-add-default-project']",
    )
    PROJECT_TITLE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Введите название проекта…']",
    )
    SUBMIT_PROJECT_BUTTON = (
        By.XPATH,
        "//div[@role='button']"
        "[.//div[contains(text(),'Добавить проект с задачами')]]",
    )
    ADD_TASK_BUTTON = (
        By.XPATH,
        "//div[@data-testid='link-button-new']"
        "[.//span[contains(text(),'Добавить задачу')]]",
    )
    TASK_TITLE_INPUT = (
        By.CSS_SELECTOR, "[data-testid='board-task-input-name']"
    )

    # --- добавлено для UI-тестов ---
    PROJECT_CARD_TITLES = (
        By.CSS_SELECTOR, "[data-testid='project-title']"
    )
    TASK_CARD_TITLES = (
        By.CSS_SELECTOR, "[data-testid='board-task-title']"
    )
    PROJECT_NAME_HEADER = (
        By.CSS_SELECTOR, "[data-testid='project-name-upper-panel']"
    )

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу проектов.

        :param driver: экземпляр веб-драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def _click(self, locator: Tuple[str, str]) -> WebElement:
        """
        Дожидается кликабельности элемента и кликает по нему через
        JavaScript. Обычный клик Selenium иногда перехватывается
        оверлеем модалки, который на долю секунды оказывается поверх
        элемента во время анимации появления — JS-клик эту гонку
        анимаций обходит.

        :param locator: локатор элемента (By, значение)
        :return: найденный элемент
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)
        return element

    def create_project(self, title: str) -> None:
        """
        Создаёт новый проект с задачами по указанному названию.

        :param title: название нового проекта
        """
        self._click(self.ADD_PROJECT_LINK)
        self._click(self.ADD_PROJECT_CARD)
        self._click(self.PROJECT_WITH_TASKS_OPTION)
        title_input = self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_TITLE_INPUT)
        )
        title_input.send_keys(title)
        self._click(self.SUBMIT_PROJECT_BUTTON)

    def click_add_task(self) -> None:
        """Нажимает кнопку добавления задачи в первой колонке."""
        self._click(self.ADD_TASK_BUTTON)

    def add_task(self, title: str) -> None:
        """
        Открывает форму добавления задачи, вводит название
        и подтверждает создание нажатием Enter.

        :param title: название новой задачи
        """
        self.click_add_task()
        task_input = self.wait.until(
            EC.visibility_of_element_located(self.TASK_TITLE_INPUT)
        )
        task_input.send_keys(title)
        task_input.send_keys(Keys.ENTER)
        task_input.send_keys(Keys.ESCAPE)
        self.wait.until(
            EC.invisibility_of_element_located(self.TASK_TITLE_INPUT)
        )

    def get_current_project_name(self) -> str:
        """
        Возвращает название проекта из шапки страницы, на которую
        Yougile перенаправляет сразу после создания проекта.

        :return: название текущего открытого проекта
        """
        header = self.wait.until(
            EC.visibility_of_element_located(self.PROJECT_NAME_HEADER)
        )
        return header.text

    def get_project_titles(self) -> List[str]:
        """
        Возвращает список названий всех видимых карточек проектов.

        :return: список заголовков проектов
        """
        self.wait.until(
            EC.presence_of_all_elements_located(self.PROJECT_CARD_TITLES)
        )
        elements = self.driver.find_elements(*self.PROJECT_CARD_TITLES)
        return [el.text for el in elements]

    def get_task_titles(self) -> List[str]:
        """
        Возвращает список названий всех видимых карточек задач
        на доске.

        :return: список заголовков задач
        """
        self.wait.until(
            EC.presence_of_all_elements_located(self.TASK_CARD_TITLES)
        )
        elements = self.driver.find_elements(*self.TASK_CARD_TITLES)
        return [el.text for el in elements]
