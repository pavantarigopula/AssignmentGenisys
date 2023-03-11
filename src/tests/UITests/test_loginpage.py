import pytest
from src.Pages.login_page import *

@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login():
    result  = login("pythonfresh1@gmail.com","Python@1234")
    assert result == "https://app.splashthat.com/events"

@pytest.mark.regression
def test_login_invalid_username():
    result = login("pythonfresh10@gmail.com", "Python@1234")
    assert result != "https://app.splashthat.com/events"

@pytest.mark.regression
def test_login_invalid_password():
    result = login("pythonfresh1@gmail.com","python44334@1234")
    assert result != "https://app.splashthat.com/events"