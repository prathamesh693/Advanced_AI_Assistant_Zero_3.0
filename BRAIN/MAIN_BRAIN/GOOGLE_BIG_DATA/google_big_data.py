from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import re
from selenium.webdriver.support.wait import WebDriverWait


def search_and_extract(text):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        # Set the path to your ChromeDriver executable
        chrome_driver_path=r'R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0\DATA\ZERO_DRIVERS\chromedriver.exe'

        chrome_service=Service(chrome_driver_path)
        driver=webdriver.Chrome(service=chrome_service, options=chrome_options)

        # Open Google in the browser
        driver.get("https://www.google.com")

        # Find the search box using its name attributes
        search_box=driver.find_element("name", "q")

        # Type the query
        search_query = text
        search_box.send_keys(search_query)

        # Submit the form
        search_box.send_keys(Keys.RETURN)

        # Wait for the search box to be present
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "q")))

        # Find the first search result element
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')

        # Extract the link of the first result
        first_result_link=first_result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

        # Visit the first result link
        driver.get(first_result_link)

        # Extract the webpage content
        webpage_content = driver.page_source

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Extract text from the webpage, excluding script and style tags
        webpage_text=' '.join([p.get_text() for p in soup.find_all('p')])

        # Extract keywords or relevant information based on your specific requirements
        # For example, you can use a keyword extraction library or manually

        # Extract and print the first 8-9 sentences from the webpage
        sentences=re.split(r'(?<=[.!?])\s',webpage_text)
        result_text='. '.join(sentences[:9])
        return result_text


    except Exception as e:
        print("An error has occurred:",e)

    except Exception as e:
        print("An error has occurred:",e)

    driver.quit()




###############################
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text,sentences_count=5):
    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document,sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

# Example usage
def summary(text):
    text_to_summarize=text
    summary_result=summarize_text(text_to_summarize)
    return summary_result

def deep_search(text):
    x=text
    y=search_and_extract(x)
    x=summary(y)
    return x
