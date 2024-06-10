import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture()
def environment():
    global driver
    driver = Firefox()
    driver.get("https://www.zendwallet.com/register")
    driver.close()

def FirstTestCase():
    driver.find_element(By.NAME,"emailAddress").send_keys("Ayobamiolabello@gmail.com")
    driver.find_element(By.NAME,"firstName").send_keys("Mosunmola")
    driver.find_element(By.NAME,"lastName").send_keys("Olabello")
    driver.find_element(By.NAME,"username").send_keys("Aybel")
    driver.find_element(By.NAME,"password").send_keys("MosunBaby")
    obj=Select(driver.find_element(By.NAME,"country"))
    obj.select_by_visible_text("Nigeria")
    driver.find_element(By.XPATH,"//span[class='chakra-checkbox__control css-1gtsxek']").click()
    driver.find_element(By.XPATH,"button[text()='Create Account']").click()