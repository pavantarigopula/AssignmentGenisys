import pytest
from src.Pages.login_page import *
import json
from pytest_bdd import scenario, given, when, then


@scenario('loginpage.feature', 'Login and select plan')
def test_login():
    pass


@given('I am on login screen')
def login():
    launch_login()


@given('Log in to application')
def login_application():
    json_file = open('configurations.json', 'r')
    user_details = json.load(json_file)
    login_user(user_details["username"], user_details["password"])


@when('Go to the Library')
def choose_library():
    select_library()


@when('Choose unlock access select plan')
def select_unlock_access():
    unlock_access_select_plan()


@then('I should be on plan demo')
def plan_demo():
    select_demo


