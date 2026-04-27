from time import sleep

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    sleep(3)
    button = driver.find_element(By.CSS_SELECTOR, "#molecule-176285426165558590 > div.t396__elem.tn-elem.t396__elem-flex.tn-elem__1921710463176285426166311940 > a")
    button.click()
    sleep(5)
    driver.save_screenshot("screenshot_itc.png")
    print("Screenshot saved")
    driver.quit()


if __name__ == "__main__":
    driver()