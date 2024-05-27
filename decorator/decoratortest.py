import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def print_current_time(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time before running {func.__name__}: {current_time}")
        return func(*args, **kwargs)
    return wrapper

@pytest.fixture(scope="module")
def driver():
    service = Service("C:/Users/lenovo/Desktop/task_selenium/decorator/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestUserInyerface:

    def test_cookies_div_icon_logo(self, driver):
        wait = WebDriverWait(driver, 10)
        eleCookiesDiv2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo__icon')))
    
        background_color = eleCookiesDiv2.value_of_css_property("background-color")

        assert background_color == "rgba(0, 0, 0, 0)", f"Expected background color rgba(0, 0, 0, 0), but got {background_color}"

    def test_cookies_div_properties(self, driver):
        wait = WebDriverWait(driver, 10)
        eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))
    
        background_color = eleCookiesDiv.value_of_css_property("background-color")
        height = float(eleCookiesDiv.size['height'])
    
        assert background_color == "rgba(255, 255, 255, 1)", "Background color is not as expected"
        assert height == 155.0, "Height is not as expected"
    
    def test_cookies_div_password(self, driver):
        wait = WebDriverWait(driver, 10)
        eleCookiesDiv3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.login-form__container')))

        background_color = eleCookiesDiv3.value_of_css_property("background-color")

        assert background_color == "rgba(255, 255, 255, 1)", "Background color is not as expected"

if __name__ == "__main__":
    pytest.main()
