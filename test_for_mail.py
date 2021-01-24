from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium.webdriver.common.by import By


class YandexAutoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\bin\chromedriver.exe')
        self.driver.get(url='https://yandex.ru/')

    def test_search_picture(self):
        driver = self.driver
        search_window = driver.window_handles[0]
        driver.find_element_by_xpath(xpath='//*[@data-id="images"]').click()

        new_window_search = driver.window_handles[1]
        driver.switch_to.window(window_name=new_window_search)

        wait = WebDriverWait(driver=driver, timeout=30)
        upload_button = wait.until(method=EC.element_to_be_clickable((By.XPATH,
                                                                      '//*[@aria-label="Поиск по изображению"]')))
        upload_button.click()

        upload_image = "автокран"
        file_input = driver.find_element_by_xpath(xpath='//*[@class="cbir-panel__file-input"]')
        file_input.send_keys(os.getcwd() + f"/{upload_image}.jpg")
        search_result = wait.until(method=EC.visibility_of_all_elements_located((By.XPATH,
                                                                                 f'//div[text() = "Кажется, на '
                                                                                 f'изображении"]/following-sibling '
                                                                                 f'::div//span[contains( text(), '
                                                                                 f'"{upload_image}")]')))

        assert search_result
