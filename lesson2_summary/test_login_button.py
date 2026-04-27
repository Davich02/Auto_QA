import pytest
from login_button import LoginButton


@pytest.fixture
def login_button():
    return LoginButton()


def test_label_is_login(login_button):
    assert login_button.get_label() == "Login"

def test_button_is_enable_by_default(login_button):
    assert login_button.is_enabled() is True

def test_button_is_disable(login_button):
    login_button.disable()
    assert login_button.is_enabled() is False

def test_button_is_enable_after_disable(login_button):
    login_button.disable()
    login_button.enable()
    assert login_button.is_enabled() is True
