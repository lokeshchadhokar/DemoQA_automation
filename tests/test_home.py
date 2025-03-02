import pytest
from selenium import webdriver
from DemoQawithJinkins.pages.home_page import HomePage

@pytest.mark.sanity
def test_navifate_to_home(driver):
    print("here is page title :",driver.title)
    assert "DEMOQA" in driver.title

@pytest.mark.regression
def test_navigate_to_element(driver):
    home_page = HomePage(driver)
    print("here is element is present :", home_page.ELEMENT)
    home_page.navigate_to_element()

@pytest.mark.smoke
def test_navigate_to_forms(driver):
    home_page = HomePage(driver)
    home_page.navigate_to_forms()
    print("here is url",driver.current_url.lower())
    assert "forms" in driver.current_url.lower()