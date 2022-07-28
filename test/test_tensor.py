import unittest

from stere import Stere
from splinter import Browser
from selenium.webdriver.common.keys import Keys
from src.pages.home_page import Home_Page


# https://github.com/cobrateam/splinter/blob/master/samples/test_google_search.py
from src.pages.search_results import Search_Results


class TensorTestCase(unittest.TestCase):
    def setUp(self):
        Stere.browser = Browser("chrome")
        Stere.url_navigator = 'visit'
        Stere.base_url = "http://www.yandex.ru/"
        self.hp = Home_Page()
        self.hp.navigate()

    def tearDown(self):
        Stere.browser.quit()

    def test_search(self):
        self.hp.search_form.click_form()
        self.hp.search_form.input_query("Тензор")

        self.hp.search_form.submit.click() #todo look for a way to actually press enter
        sr = Search_Results()
        top_result = sr.get_top_result()
        assert 'tensor.ru' in top_result.link.element['href']

    def test_pictures(self):
        self.hp.navigation.click_navigation("Картинки", True, Stere.browser)

