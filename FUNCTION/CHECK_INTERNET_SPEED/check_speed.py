import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from FUNCTION.ZERO_SPEAK.speak import speak


def get_internet_speed():
    try:
        # Set the path to your ChromeDriver executable
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_driver_path = r'R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\ZERO_DRIVERS\chromedriver.exe'

        # Initialize Chrome browser
        service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the websites
        driver.get("https://fast.com/")
        speak("Checking Internet Speed, sir")
        time.sleep(11)

        # Wait for the speed test to complete
        WebDriverWait(driver,timeout=60).until(EC.presence_of_element_located((By.ID,"speed-value")))

        # Find the element with the speed value
        speed_element=driver.find_element(By.ID,value="speed-value")

        # Get the text value from the element
        speed_value=speed_element.text

        return speed_value
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Close the browser window
        if driver:
            driver.quit()

def check_internet_speed():
    speed_result=get_internet_speed()

    if speed_result is not None:
        speak(f'sir, your internet speed is: {speed_result} Mbps')
    else:
        speak("Error: Unable to get internet speed.")

#check_internet_speed()