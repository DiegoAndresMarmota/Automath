from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website_page = ('WEBSITE_HERE')
path = ('MY_CHROME_DRIVER_HERE')

driver =webdriver.Chrome(service=service)
service = Service(executable_path=path)
driver.get(website_page)