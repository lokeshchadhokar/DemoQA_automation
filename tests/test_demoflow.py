import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    yield driver  # Ensures proper cleanup
    driver.quit()  # Closes the browser after test execution

def test_navigate_to_Elemnt(setup):
    diplay = setup.find_element(By.XPATH,'//div[@class="card-body"]/h5[text()="Elements"]')
    assert diplay.is_displayed(), "Element is not display"

def test_navigate_to_forms(setup):
    try:
        # Wait for the 'Forms' section to be visible and clickable
        element = WebDriverWait(setup, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))
        )
        setup.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    except Exception as e:
        pytest.fail(f"Test failed due to: {str(e)}")

