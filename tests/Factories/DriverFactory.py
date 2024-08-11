from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

def get_driver():
  return webdriver.Chrome()
