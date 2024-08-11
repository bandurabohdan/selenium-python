import os

from selenium.webdriver.remote.webdriver import WebDriver

from Pages.BasePage import BasePage

class SignInPage(BasePage):
  def __init__(self, driver: WebDriver) -> None:
    super().__init__(driver)

  def enter_sign_in_data(self) -> None:
    self.type('input[placeholder="Email"]', os.getenv('USER_EMAIL'))
    self.type('input[placeholder="Password"]', os.getenv('USER_PASSWORD'))

  def click_sign_in_button(self) -> None:
    self.click('button[type="submit"]')

  def login(self) -> None:
    self.enter_sign_in_data()
    self.click_sign_in_button()
    self.is_user_signed_in(os.getenv('USERNAME'))


  # async loginUsingAPI() {

  #   let response = await fetch(`${process.env.BASE_API_URL}/users/login`, {
  #     method: 'POST',
  #     headers: {'Content-Type': 'application/json'},
  #     body: JSON.stringify({
  #       user: {
  #         email: process.env.USER_EMAIL,
  #         password: process.env.USER_PASSWORD
  #       }
  #     })
  #   })

  #   response = await response.json()

  #   const { username, email, token } = response.user

  #   expect(username).to.eq(process.env.USERNAME)
  #   expect(email).to.eq(process.env.USER_EMAIL)
  #   expect(token).to.be.a('string')

  #   return token
  # }
