import time
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = Chrome(executable_path=ChromeDriverManager().install())
web = "https://demo.guru99.com/test/newtours/register.php"


def test_web_page():
    driver.get(web)
    name = 'max'
    last = 'Hv'
    user = 'Python Master'
    field_first_name = driver.find_element(By.NAME, 'firstName').send_keys(name)
    field_last_name = driver.find_element(By.NAME, 'lastName').send_keys(last)
    field_phone = driver.find_element(By.NAME, 'phone').send_keys('+9 582 457825')
    field_email = driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys('max@google.com')
    field_address = driver.find_element(By.NAME, 'address1').send_keys('Rafieva str.')
    field_city = driver.find_element(By.NAME, 'city').send_keys('Minsk')
    field_state = driver.find_element(By.NAME, 'state').send_keys('Alabama')
    field_postal_code = driver.find_element(By.NAME, 'postalCode').send_keys('550017')
    field_country = Select(driver.find_element(By.XPATH, "//select[@name='country']"))
    field_country.select_by_value("BELARUS")
    field_user_name = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(user)
    field_password = driver.find_element(By.NAME, 'password').send_keys('qwerty')
    field_confirm_password = driver.find_element(By.NAME, 'confirmPassword').send_keys('qwerty')
    button = driver.find_element(By.XPATH, "//input[@name='submit']").click()
    text_name = driver.find_element(By.XPATH, "//p[1]//font[b]").text
    except_name = text_name.split(' ')
    assert except_name[1] == name
    assert except_name[2][:-1] == last
    text_user_name = driver.find_element(By.XPATH, "//p[3]//font[b]").text
    except_user = text_user_name.split(' ')
    except_user = except_user[5:]
    except_user = ' '.join(except_user)[:-1]
    assert except_user == user
    time.sleep(4)
    driver.close()
