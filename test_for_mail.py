import pytest
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
        file_input.send_keys(os.getcwd() + "/автокран.jpg")
        driver.implicitly_wait(20)
        search_result = driver.find_element_by_xpath(xpath='//span[@class="Button2-Text" and contains(text(//div[text() = "Кажется, на изображении"]/following-sibling::div//span[contains(text(),"{upload_image}")]')

        assert search_result == upload_image


