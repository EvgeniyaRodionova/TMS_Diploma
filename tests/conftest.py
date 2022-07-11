import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def chrome_options():
    options = Options()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    return options


@pytest.fixture(scope="session")
def browser(chrome_options):
    options = chrome_options
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 800)
    return driver






