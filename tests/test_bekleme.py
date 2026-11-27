from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.xfail(reason="Bekleme yok: yazı henüz görünmeden okunuyor")
def test_beklemeden(driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        yazi = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
        assert yazi == "Hello World!"

def test_explicit_wait(driver):
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        yazi = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    ).text
        assert yazi == "Hello World!"