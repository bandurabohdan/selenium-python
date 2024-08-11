import pytest
import time
import os

from Factories.DriverFactory import get_driver
from Factories.PageFactory import PageFactory

@pytest.fixture
def page_factory(request):
  driver = get_driver()
  page_factory = PageFactory(driver)
  test_title = request.node.name
  home_page = page_factory.get_home_page()
  sign_in_page = page_factory.get_sign_in_page()

  driver.get(os.getenv('BASE_URL'))

  if 'sign_up' not in test_title:
    home_page.open_sign_in_page()
  else:
    home_page.open_sign_up_page()

  if 'sign_in' not in test_title and 'sign_up' not in test_title:
    sign_in_page.login()

  yield page_factory

  if request.node.rep_call.failed:

    screenshot_dir = './failed_screenshots'

    if not os.path.exists(screenshot_dir):
      os.makedirs(screenshot_dir)

    screenshot_title = f"{test_title}_{time.time()}.png"
    driver.save_screenshot(f"{screenshot_dir}/{screenshot_title}")

  driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
