import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser)

# Specify the path to your Chrome driver executable

chrome_driver_path = r'R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\ZERO_DRIVERS\chromedriver.exe'

# Create a Service object with the specified executable path
chrome_service = Service(chrome_driver_path)

# Create a Chrome driver instance with the specified options and service
driver= webdriver.Chrome(service=chrome_service,options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")

# Navigate to the website

def speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')))

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        element_to_click.send_keys(text)
        print(text)

        # Calculate sleep duration based on sentence length
        sleep_duration = min(0.2 + len(text) // 20, 50)

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]')))

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print(f"Error in speak(): {e}")

# speak("hello world")