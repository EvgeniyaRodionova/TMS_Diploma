from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.find_element(By.NAME, "firstName").send_keys("Evgeniya")
driver.find_element(By.NAME, "lastName").send_keys("Rodionova")
driver.find_element(By.NAME, "phone").send_keys("+375295869977")
driver.find_element(By.NAME, "userName").send_keys("evgeniya.rodionova@gmail.com")
driver.find_element(By.NAME, "address1").send_keys("Garuna 16-61")
driver.find_element(By.NAME, "city").send_keys("Minsk")
driver.find_element(By.NAME, "postalCode").send_keys("220055")

country_drop = Select(driver.find_element(By.NAME, "country"))
country_drop.select_by_value("BELARUS")

driver.find_element(By.NAME, "email").send_keys("EvgeniyaRo")
driver.find_element(By.NAME, "password").send_keys("12345")
driver.find_element(By.NAME, "confirmPassword").send_keys("12345")

button = driver.find_element(By.NAME, "submit")
button.click()

driver.get("https://demo.guru99.com/test/newtours/register_sucess.php")
full_name = driver.find_element(By.XPATH, "//font/b[1]").text
assert "Dear Evgeniya Rodionova," == full_name

user_name = driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b").text
assert "Note: Your user name is EvgeniyaRo." == user_name









