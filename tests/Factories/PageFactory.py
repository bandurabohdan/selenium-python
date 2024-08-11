from Pages.HomePage import HomePage
from Pages.SignUpPage import SignUpPage
from Pages.SignInPage import SignInPage
from Pages.ArticlePage import ArticlePage
from Pages.ProfilePage import ProfilePage

class PageFactory:
  def __init__(self, driver) -> None:
    self.driver = driver

  def get_home_page(self) -> HomePage:
    return HomePage(self.driver)

  def get_sign_up_page(self) -> SignUpPage:
    return SignUpPage(self.driver)

  def get_sign_in_page(self) -> SignInPage:
    return SignInPage(self.driver)

  def get_article_page(self) -> ArticlePage:
    return ArticlePage(self.driver)

  def get_profile_page(self) -> ProfilePage:
    return ProfilePage(self.driver)
