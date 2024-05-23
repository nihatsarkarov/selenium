from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Replace the path with the correct path to your ChromeDriver executable
service = Service("C:/Users/lenovo/Desktop/task_selenium/chromedriver.exe")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://userinyerface.com/game.html")

input("Press Enter to close the browser...")

driver.quit()
