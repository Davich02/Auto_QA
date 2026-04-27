import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Открывает https://itcareerhub.de/ru
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    sleep(1)
    yield driver
    driver.quit()


#Логотип ITCareerHub
def test_logo(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "#rec1921710463 > div > div > div.t396__elem.tn-elem.tn-elem__19217104631710153310155 > a")
    assert logo.is_displayed() is True

#Ссылка “Программы”
def test_link_programs(driver):
    link = driver.find_element(By.LINK_TEXT,"Программы")
    assert link.is_displayed() is True

#Ссылка “Способы оплаты”
def test_link_payment_method(driver):
    link = driver.find_element(By.LINK_TEXT,"Способы оплаты")
    assert link.is_displayed() is True


#Ссылка “О нас”
def test_link_about(driver):
    link = driver.find_element(By.LINK_TEXT,"О нас")
    assert link.is_displayed() is True

#Ссылка “Контакты”
def test_link_contacts(driver):
    about = driver.find_element(By.LINK_TEXT, "О нас")
    about.click()
    link = driver.find_element(By.LINK_TEXT, "Контакты")
    assert link.is_displayed() is True

#Ссылка “Отзывы”
def test_link_reviews(driver):
    link = driver.find_element(By.LINK_TEXT, "Отзывы")
    assert link.is_displayed() is True


#Ссылка “Блог”
def test_blog(driver):
    link = driver.find_element(By.LINK_TEXT, "Блог")
    assert link.is_displayed() is True

#Кнопки переключения языка (ru и de)
def test_lang_ru(driver):
    btn = driver.find_element(By.LINK_TEXT, "ru")
    assert btn.is_displayed() is True

def test_lang_de(driver):
    btn = driver.find_element(By.LINK_TEXT, "de")
    assert btn.is_displayed() is True

#Кликнуть по разделу “Контакты”
#Кликнуть по кнопке “Обратный звонок”
#Проверить что текст “Запишитесь на бесплатную карьерную консультацию” отображается во всплывающем окне.
def test_click_contacts(driver):
    about = driver.find_element(By.LINK_TEXT, "О нас")
    about.click()
    contacts = driver.find_element(By.LINK_TEXT, "Контакты")
    contacts.click()
    sleep(3)
    callback_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")
    driver.execute_script("arguments[0].click();", callback_btn)
    sleep(3)
    popup = driver.find_element(By.CSS_SELECTOR, ".t-popup_show")
    assert "Запишитесь на бесплатную карьерную консультацию" in popup.text