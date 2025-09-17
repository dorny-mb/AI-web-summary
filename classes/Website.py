
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


class Website:
    def __init__(self, url: str, use_selenium=False):
        self.url = url

        if use_selenium:
            self.html = self._fetch_with_selenium()
        else:
            self.html = self._fetch_with_requests()

      
        soup = BeautifulSoup(self.html, "html.parser")
        self.title = soup.title.string if soup.title else "No Title Found"
        for irrelevant in soup(["script", "style", 'img', 'input']):
            irrelevant.decompose()

        self.text = soup.body.get_text(separator='\n', strip=True)
    def _fetch_with_requests(self):
        response = requests.get(self.url, headers=headers)
        return response.text
    def _fetch_with_selenium(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get(self.url)
        time.sleep(5)  # Wait for JavaScript to load content

        html = driver.page_source
        driver.quit()
        return html