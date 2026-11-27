from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com/"


def test_basarili_giris(driver):
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    assert "inventory" in driver.current_url


def test_yanlis_sifre(driver):
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("yanlis123")
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    hata = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in hata.text
    