import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login(username,password):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get("https://splashthat.com/login")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "homeRealmDiscoveryInput").send_keys(username)
    driver.find_element(By.ID, "homeRealmDiscoverySubmit").click()
    time.sleep(10)
    driver.find_element(By.ID, "loginPasswordInput").send_keys(password)
    driver.find_element(By.ID, "loginSubmit").click()
    time.sleep(10)
    return driver.current_url
