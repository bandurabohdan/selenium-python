from typing import Union
import allure

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
  def __init__(self, driver: WebDriver) -> None:
    self.driver = driver

  @allure.step('Navigating to {link}')
  def navigate_to(self, link: str):
    self.driver.get(link)

  def is_user_signed_in(self, user_name: str):
    user_name_nav_link = self.get_text('a.nav-link[href^="/profile"]')
    assert user_name_nav_link.lower() == user_name.lower()

  def get_element(self, selector: str) -> WebElement:
    get_by = By.XPATH if selector[0] == '/' else By.CSS_SELECTOR

    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((get_by, selector)))
    element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((get_by, selector)))
    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    return element

  def get_elements(self, selector: str) -> list[WebElement]:
    get_by = By.XPATH if selector[0] == '/' else By.CSS_SELECTOR

    elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((get_by, selector)))
    elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((get_by, selector)))
    self.driver.execute_script("arguments[0].scrollIntoView(true);", elements[0])

    return elements

  def get_element_by_text(self, text: str) -> WebElement:
    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), {text})]")))
    element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), {text})]")))
    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    return element

  @allure.step('Click on element {selector}')
  def click(self, selector: Union[str, WebElement]) -> None:
    if type(selector) is not str:
      selector.click()
      return

    element = self.get_element(selector)
    element.click()

  @allure.step('Type in element {selector}')
  def type(self, selector: Union[str, WebElement], text: str) -> None:
    if type(selector) is not str:
      selector.send_keys(text)
      return

    element = self.get_element(selector)
    element.send_keys(text)

  @allure.step('Getting text from element {selector}')
  def get_text(self, selector: Union[str, WebElement]) -> str:
    element = None
    result = None

    if type(selector) is not str:
      result = selector.text
      return

    element = self.get_element(selector)
    result = element.text

    return result

  def quit_driver(self) -> None:
    self.driver.quit()
