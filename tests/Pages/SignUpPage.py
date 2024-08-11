from faker import Faker
import time

from selenium.webdriver.remote.webdriver import WebDriver

from Pages.BasePage import BasePage

class SignUpPage(BasePage):
  def __init__(self, driver: WebDriver) -> None:
    super().__init__(driver)
    self.fake = Faker()
    self.first_name = self.fake.first_name()
    self.last_name = self.fake.last_name()
    self.user_name = f"{self.first_name}_{self.last_name}"

  def enter_sign_up_data(self, user_name: str, last_name: str) -> None:
    self.type('input[placeholder="Username"]', user_name)
    self.type('input[placeholder="Email"]', f"{last_name}_{time.time()}@gmail.com")
    self.type('input[placeholder="Password"]', last_name)

  def click_sign_up_button(self) -> None:
    self.click('button[type="submit"]')

  def register(self) -> None:
    self.enter_sign_up_data(self.user_name, self.last_name)
    self.click_sign_up_button()
    self.is_user_signed_in(self.user_name)
