#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'filter_class')))
        star_filtration_box = self.driver.find_element_by_id('filter_class')
        # star_filtration_box = self.driver.find_element_by_css_selector(
        #     'div[data-id="filter_class"]'
        # )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        try:
            for star_value in star_values:
                for star_element in star_child_elements:
                    self.driver.implicitly_wait(10)
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                        star_element.click()
        except Exception as e:
            print(f"Error Found : {e}")


    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()