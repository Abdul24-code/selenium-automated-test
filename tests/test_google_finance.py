import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.google_finance_page import GoogleFinancePage

class TestGoogleFinance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set Chrome options to run in headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (required for some environments)
        chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging

        # Initialize Chrome WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.google_finance_page = GoogleFinancePage(cls.driver)

    def test_google_finance_stocks(self):
        # Step 1: Open the webpage
        self.google_finance_page.load()

        # Step 2: Verify the page title
        self.assertIn("Google Finance", self.google_finance_page.get_page_title())

        # Step 3: Retrieve stock symbols
        retrieved_symbols = self.google_finance_page.get_stock_symbols()
        given_test_data = ["NFLX", "MSFT", "TSLA"]

        # Step 4: Compare retrieved symbols with given test data
        symbols_in_ui_not_in_data = set(retrieved_symbols) - set(given_test_data)
        symbols_in_data_not_in_ui = set(given_test_data) - set(retrieved_symbols)

        # Step 5: Print the differences
        print("Stock symbols in UI but not in given test data:", symbols_in_ui_not_in_data)
        print("Stock symbols in given test data but not in UI:", symbols_in_data_not_in_ui)

    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
