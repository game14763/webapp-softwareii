from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Web Title', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Web Header', header_text)

        inputbox = self.browser.find_element_by_id('username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Username'
        )
        inputbox.send_keys('myid')

        inputbox = self.browser.find_element_by_id('password')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'
        )
        inputbox.send_keys('mypassword')

        inputbox.send_keys(Keys.ENTER)
        """
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        """
