import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.google_finance_page import GoogleFinancePage

class TestGoogleFinance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")

        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.google_finance_page = GoogleFinancePage(cls.driver)

    def test_google_finance_stocks(self):
        print("Loading Google Finance page...")
        self.google_finance_page.load()

        print("Verifying the page title...")
        self.assertIn("Google Finance", self.google_finance_page.get_page_title())

        print("Retrieving stock symbols...")
        try:
            pass
            retrieved_symbols = self.google_finance_page.get_stock_symbols()
            print("Retrieved symbols:", retrieved_symbols)
        except Exception as e:
            print("Error while retrieving stock symbols:", e)
            raise e

        given_test_data = ["NFLX", "MSFT", "TSLA"]

        symbols_in_ui_not_in_data = set(retrieved_symbols) - set(given_test_data)
        symbols_in_data_not_in_ui = set(given_test_data) - set(retrieved_symbols)

        print("Stock symbols in UI but not in given test data:", symbols_in_ui_not_in_data)
        print("Stock symbols in given test data but not in UI:", symbols_in_data_not_in_ui)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
