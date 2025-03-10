import pytest
from selenium import webdriver
import yaml

@pytest.fixture(scope="session")
def config():
    with open("../config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver(config):
    if config["browser"] == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Browser {config['browser']} not supported!")
    driver.get(config["url"])
    driver.maximize_window()
    yield driver
    driver.quit()
