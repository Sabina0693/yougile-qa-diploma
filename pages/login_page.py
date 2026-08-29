from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница входа в Yougile."""

    URL = "https://ru.yougile.com/team"

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (
        By.XPATH,
        "//div[@role='button'][.//div[contains(text(),'Войти')]]",
    )

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу входа.

        :param driver: экземпляр веб-драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open(self) -> None:
        """Открывает страницу входа в браузере."""
        self.driver.get(self.URL)
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )

    def login(self, email: str, password: str) -> None:
        """
        Выполняет вход в систему по email и паролю.

        :param email: адрес электронной почты
        :param password: пароль пользователя
        """
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_input.send_keys(email)

        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
