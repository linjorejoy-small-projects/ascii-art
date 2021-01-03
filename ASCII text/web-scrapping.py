from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# driver = webdriver.Chrome("C:/Users/LINJO/Downloads/chromedriver")
URL = 'https://manytools.org/facebook-twitter/ascii-banner-2/'
page_request = requests.get(URL)
soup = BeautifulSoup(page_request.content, 'html.parser')
fonts = soup.find(id="Form_Font")
print(fonts)
