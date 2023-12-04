import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SaucedemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_1_login_with_valid_credentials(self):
        # Test Case 1 implementation
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Validation
        product_page_title = self.driver.find_element(By.CLASS_NAME, "title").text
        self.assertEqual(product_page_title, "Products")

    def test_2_sort_products_on_product_page(self):
        # Test Case 2 implementation
        sort_dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()

        price_low_to_high_option = self.driver.find_element(By.XPATH, "//option[text()='Price (low to high)']")
        price_low_to_high_option.click()

        # Validation
        product_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text[1:]) for price in product_prices]
        self.assertTrue(all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1)))

    def test_3_add_product_to_cart(self):
        # Test Case 3 implementation
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        product_name_xpath = "/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div"
        
        # Wait for the element to be present
        element_present = EC.presence_of_element_located((By.XPATH, product_name_xpath))
        WebDriverWait(self.driver, 2).until(element_present)

        # Find the element
        product_name_element = add_to_cart_buttons[0].find_element(By.XPATH, product_name_xpath)
        product_name = product_name_element.text

        add_to_cart_buttons[0].click()

        # Validation
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_icon.text, "1")

        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

        cart_product_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_product_names = [name.text for name in cart_product_names]
        self.assertIn(product_name, cart_product_names)

    def test_4_login_with_invalid_credentials(self):
        # Check if the user is already logged in
        try:
            cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

            # User is already logged in, perform logout
            hamburger_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
            hamburger_button.click()

            WebDriverWait(self.driver, timeout=2).until(lambda d : hamburger_button.is_displayed())

            logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
            logout_button.click()

            # Wait for the login page to load after logout
            WebDriverWait(self.driver, 10).until(EC.title_contains("Swag Labs"))

        except NoSuchElementException:
            # User is not logged in, continue with login test
            pass

        # Rest of the Test Case 4 implementation (login with invalid credentials)
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username_input.send_keys("invalid_user")
        password_input.send_keys("invalid_password")
        login_button.click()

        # Validation
        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))