# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class GoogleFinancePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://www.google.com/finance"
#         # Updated XPath locator for the section "You may be interested in"
#         self.stock_section_locator = "//div[contains(text(),'You may be interested in')]"

#     def load(self):
#         self.driver.get(self.url)

#     def get_page_title(self):
#         return self.driver.title

#     def get_stock_symbols(self):
#         # Wait for the section to be visible
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((By.XPATH, self.stock_section_locator))
#         )
#         # Example of finding stock symbols based on a more specific XPath or CSS selector
#         stock_elements = self.driver.find_elements(By.XPATH, "//a[@class='EIXGkd']")  # Adjusted XPath
#         return [stock.text for stock in stock_elements if stock.text]
#=======================

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"
        # Update the locator for the entire "You may be interested in" section
        self.stock_section_locator = "//div[contains(@class, 'EZ06yb')]"

    def load(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title

    def get_stock_symbols(self):
        # Wait until the section containing stock symbols is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.stock_section_locator))
        )
        # Update to find stock symbols more precisely
        stock_elements = self.driver.find_elements(By.XPATH, "//a[@class='QYdxV']")  # Adjusted XPath
        return [stock.text for stock in stock_elements if stock.text]
