import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "kullanici, sifre, basarili_mi, beklenen_hata",
    [
        ("standard_user", "secret_sauce", True, None),
        ("problem_user", "secret_sauce", True, None),
        ("locked_out_user", "secret_sauce", False, "locked out"),
        ("standard_user", "yanlis123", False, "Username and password do not match"),
    ],
)
def test_login(driver, kullanici, sifre, basarili_mi, beklenen_hata):
    sayfa = LoginPage(driver)
    sayfa.ac()
    sayfa.giris_yap(kullanici, sifre)

    if basarili_mi:
        assert "inventory" in driver.current_url
    else:
        assert beklenen_hata in sayfa.hata_mesaji()