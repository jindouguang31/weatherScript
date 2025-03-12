from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.hko.MyObservatory_v1_0",
        "appActivity": ".MyObservatory",
        "noReset": True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

def test_9th_day_forecast(driver):
    # Navigate to the 9-day forecast screen
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "9-Day Forecast").click()
    
    # Scroll to the 9th day
    for _ in range(8):
        driver.swipe(500, 1500, 500, 500, 400)
    
    # Get the 9th day's forecast
    ninth_day_forecast = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Day 9')]").text
    assert "Day 9" in ninth_day_forecast