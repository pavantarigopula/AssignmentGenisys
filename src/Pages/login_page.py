import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_obj = webdriver.Chrome("chromedriver.exe")
driver_obj.maximize_window()


def launch_login():
    driver_obj.get("https://splashthat.com/login")


def login_user(username, password):
    driver_obj.implicitly_wait(10)
    time.sleep(30)
    driver_obj.find_element(By.ID, "homeRealmDiscoveryInput").send_keys(username)
    driver_obj.find_element(By.ID, "homeRealmDiscoverySubmit").click()
    driver_obj.find_element(By.ID, "loginPasswordInput").send_keys(password)
    driver_obj.find_element(By.ID, "loginSubmit").click()
    time.sleep(10)


def select_library():
    driver_obj.find_element(By.XPATH, "//span[normalize-space()='Library']").click()


def unlock_access_select_plan():
    driver_obj.find_element(By.XPATH, "//div[contains(text(),'Unlock Access')]").click()
    time.sleep(10)
    handles = driver_obj.window_handles
    driver_obj.switch_to.window(handles[1])
    time.sleep(10)
    driver_obj.find_element(By.XPATH, "//a[normalize-space()='Get Splash Pro']").click()


def select_demo():
    handles = driver_obj.window_handles
    driver_obj.switch_to(handles[1])
    time.sleep(10)
