'''Написать скрипт, который:
Переходит на https://the-internet.herokuapp.com/login
Вводит email
Вводит password'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pytest

login = "tomsmith"
password = "SuperSecretPassword!"

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_login(driver):
    username = driver.find_element(By.CSS_SELECTOR, "#username")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password")
    username.send_keys(login)
    password_field.send_keys(password)
#   sleep(5)
    '''Совершить клик на кнопку Submit
    Проверить изменение в URL
    Проверить наличие текста "You logged into a secure area!"'''
    btn_submit = driver.find_element(By.CSS_SELECTOR, "#login > button > i")
    btn_submit.click()
    sleep(2)
#    cur_url = driver.curent_url
    text = driver.find_element(By.CSS_SELECTOR, "#flash").text
    assert "https://the-internet.herokuapp.com/secure" in driver.current_url
    assert "You logged into a secure area!" in text


'''Написать новый авто-тест со следующими условиями:
Проверить неправильно введенный username'''

def test_failed_login(driver):
    username = driver.find_element(By.CSS_SELECTOR, "#username")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password")
    username.send_keys("falshlogin")
    password_field.send_keys(password)
    btn_submit = driver.find_element(By.CSS_SELECTOR, "#login > button > i")
    btn_submit.click()
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, "#flash").text
    assert "Your username is invalid!" in text
