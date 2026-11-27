def test_selenium_basligi(driver):
    driver.get("https://www.selenium.dev")

    assert "Selenium" in driver.title


def test_bilerek_fail(driver):
    driver.get("https://www.selenium.dev")

    assert "Google" in driver.title     