from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"

    KULLANICI_ADI = (By.ID, "user-name")
    SIFRE = (By.CSS_SELECTOR, "#password")
    GIRIS_BUTONU = (By.XPATH, "//input[@id='login-button']")
    HATA_MESAJI = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def ac(self):
        self.driver.get(self.URL)

    def giris_yap(self, kullanici, sifre):
        self.driver.find_element(*self.KULLANICI_ADI).send_keys(kullanici)
        self.driver.find_element(*self.SIFRE).send_keys(sifre)
        self.driver.find_element(*self.GIRIS_BUTONU).click()

    def hata_mesaji(self):
        return self.driver.find_element(*self.HATA_MESAJI).text