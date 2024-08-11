import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from Pages.BasePage import BasePage

class ProfilePage(BasePage):
  def __init__(self, driver: WebDriver) -> None:
    super().__init__(driver)

  def open_favorites_posts_tab(self) -> None:
    favorite_posts_tab = self.get_element_by_text('My Posts')
    self.click(favorite_posts_tab)

  def open_my_posts_tab(self) -> None:
    my_posts_tab = self.get_element_by_text('Favorited Posts')
    self.click(my_posts_tab)

  def get_articles(self) -> list[WebElement]:
    return self.get_elements('div[class="article-preview"]')

  def get_article_title(self, article: str) -> str:
    return self.get_text(article)

  def is_article_added(self, expectedTtitle: str) -> None:
    self.driver.refresh()
    time.sleep(1)
    article_title = self.get_article_title('div[class="article-preview"]:nth-child(2) h1')
    assert article_title.lower() == f"article title: {expectedTtitle.lower()}"
