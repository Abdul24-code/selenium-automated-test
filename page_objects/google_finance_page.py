from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleFinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/finance"
        self.stock_section_locator = "//div[contains(text(),'You may be interested in')]"

    def load(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title

    def get_stock_symbols(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.stock_section_locator))
        )
        stock_elements = self.driver.find_elements(By.XPATH, "//*[@class='COaKTb']")  # Example XPath for stock symbols
        return [stock.text for stock in stock_elements]
