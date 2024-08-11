from selenium.webdriver.remote.webdriver import WebDriver

from Pages.BasePage import BasePage

class HomePage(BasePage):
  def __init__(self, driver: WebDriver) -> None:
    super().__init__(driver)

  def open_sign_up_page(self) -> None:
    self.click('a[href="/user/register"]')

  def open_sign_in_page(self) -> None:
    self.click('a[href="/user/login"]')

  def open_article_page(self) -> None:
    self.click('a[href="/editor"]')

  def open_profile_page(self) -> None:
    self.click('a.nav-link[href^="/profile"]')
