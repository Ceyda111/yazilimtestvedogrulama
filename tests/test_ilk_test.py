import pytest

def test_selenium_basligi(driver):
    driver.get("https://www.selenium.dev")

    assert "Selenium" in driver.title


@pytest.mark.xfail(reason="Bilerek başarısız: başlıkta 'Google' yok")
def test_bilerek_fail(driver):
    driver.get("https://www.selenium.dev")

    assert "Google" in driver.title     