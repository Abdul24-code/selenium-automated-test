from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"
        # Update the locator for the stock symbols section
        self.stock_section_locator = "//div[contains(@class, 'EZ06yb')]"  # Adjusted class name or identifier

    def load(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title

    def get_stock_symbols(self):
        # Wait for the stock symbols section to be visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.stock_section_locator))
        )
        # Adjust the locator to find stock symbols more accurately
        stock_elements = self.driver.find_elements(By.XPATH, "//a[@class='QYdxV']")  # Update to the correct class or attribute
        return [stock.text for stock in stock_elements if stock.text]
