import pytest
from src.Pages.signup_page import *

@pytest.mark.smoke
@pytest.mark.regression
def test_signup():
    result  = signup()
    assert result == "https://app.splashthat.com/login/verifyEmail"

