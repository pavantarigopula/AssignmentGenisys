import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def signup():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.maximize_window()
    driver.get("https://splashthat.com/login")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//a[@class='sign-up-block__link']").click()

    driver.find_element(By.ID, "signupFullNameInput").send_keys("test t")
    driver.find_element(By.ID, "signupEmailInput").send_keys("test12@gmail.com")
    driver.find_element(By.ID,"signupPasswordInput").send_keys("Test@12345")
    driver.find_element(By.ID,"privacyPolicyInput").click()
    driver.find_element(By.ID, "signupSubmit").click()
    time.sleep(10)
    return driver.current_url
