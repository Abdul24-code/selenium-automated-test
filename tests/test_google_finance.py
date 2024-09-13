import unittest
from selenium import webdriver
from page_objects.google_finance_page import GoogleFinancePage  # Assuming you saved the POM in a folder named page_objects

class TestGoogleFinance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome WebDriver
        cls.driver = webdriver.Chrome()
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
