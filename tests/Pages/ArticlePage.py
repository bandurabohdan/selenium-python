from faker import Faker

from selenium.webdriver.remote.webdriver import WebDriver

from Pages.BasePage import BasePage

class ArticlePage(BasePage):
  def __init__(self, driver: WebDriver) -> None:
    super().__init__(driver)
    self.fake = Faker()
    self.article_title = self.fake.slug()
    self.article_description = self.fake.sentence()
    self.article_body = self.fake.paragraph()

  def enter_article_data(self) -> str:
    self.type('input[placeholder="Article Title"]', self.article_title)
    self.type('input[placeholder="What\'s this article about?"]', self.article_description)
    self.type('textarea[placeholder="Write your article (in markdown)"]', self.article_body)

    return self.article_title

  def click_publish_article(self) -> None:
    self.click('button[type="button"]')

  def publish_article(self) -> str:
    article_title = self.enter_article_data()
    self.click_publish_article()

    return article_title

  # async publishArticleUsingAPI(token) {
  #   let response = fetch(`${process.env.BASE_API_URL}/articles`, {
  #     method: 'POST',
  #     headers: {'Content-Type': 'application/json', 'Authorization': `Token ${token}`},
  #     body: JSON.stringify({
  #       article: {
  #         title: self.articleTitle,
  #         description: self.articleDescription,
  #         body: self.articleBody,
  #         tagList: []
  #       }
  #     })
  #   })

  #   response = response.json()

  #   const { slug, title, description, body, tagList, author } = response.article

  #   expect(slug).to.contains(self.articleTitle.toLowerCase())
  #   expect(title).to.eq(self.articleTitle.toLowerCase())
  #   expect(description).to.eq(self.articleDescription)
  #   expect(body).to.eq(self.articleBody)
  #   expect(tagList).to.be.an('array').that.is.empty
  #   expect(author.username).to.eq(process.env.USERNAME)

  # }
