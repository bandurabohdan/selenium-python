from Factories.PageFactory import PageFactory

class TestSuit():

  def test_sign_up_new_user(self, page_factory: PageFactory):
    sign_up_page = page_factory.get_sign_up_page()
    sign_up_page.register()

  def test_sign_in_with_existing_user(self, page_factory: PageFactory):
    sign_in_page = page_factory.get_sign_in_page()
    sign_in_page.login()

  def test_create_article(self, page_factory: PageFactory):
    home_page = page_factory.get_home_page()
    article_page = page_factory.get_article_page()
    profile_page = page_factory.get_profile_page()

    home_page.open_article_page()
    article_title = article_page.publish_article()
    home_page.open_profile_page()
    profile_page.is_article_added(article_title)
